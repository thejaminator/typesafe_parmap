import time
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

from typesafe_parmap import par_map_timeout_n
from typesafe_parmap.parmap_timeout import par_map_timeout_2


def long_running_int(param: int) -> int:
    time.sleep(10)  # long IO task here that should tiemout
    return param


def short_running_str(param: str, sleep_seconds: int = 1) -> str:
    time.sleep(sleep_seconds)
    return param


def test_timeout_parmap():
    executor = ThreadPoolExecutor(2)
    int_result, str_result = par_map_timeout_2(
        func1=lambda: long_running_int(5),
        func2=lambda: short_running_str("test"),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    assert int_result is None
    assert str_result == "test"

    # Threadpool should still be alive so it should be able to run this
    str_result_1, str_result_2 = par_map_timeout_2(
        func1=lambda: short_running_str("test 1"),
        func2=lambda: short_running_str("test 2"),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    assert str_result_1 == "test 1"
    assert str_result_2 == "test 2"


def test_timeout_parmap_3_threads():
    # Since there are 3 threads, we should be able to run 3 functions at once
    executor = ThreadPoolExecutor(3)
    int_result, str_result_1, str_result_2 = par_map_timeout_n(
        lambda: long_running_int(5),
        lambda: short_running_str("test 1", sleep_seconds=1),
        lambda: short_running_str("test 2", sleep_seconds=1),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    assert int_result is None
    assert str_result_1 == "test 1"
    assert str_result_2 == "test 2"


def test_timeout_parmap_1_thread():
    # Since there is only 1 thread, we should only be able to run 1 function at a time
    executor = ThreadPoolExecutor(1)
    int_result, str_result_1, str_result_2 = par_map_timeout_n(
        func1=lambda: long_running_int(5),
        func2=lambda: short_running_str("test 1", sleep_seconds=1),
        func3=lambda: short_running_str("test 2", sleep_seconds=1),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    assert int_result is None
    assert str_result_1 is None, "The second function should have timed out since there is only 1 thread"
    assert str_result_2 is None, "The third function should have timed out since there is only 1 thread"


def test_timeout_overall_2():
    # The timeout should be applied overall
    # We limit the timeout to 4 seconds
    # Each function takes 3 seconds
    # So the parmap should timeout after 4 seconds, not 8

    executor = ThreadPoolExecutor(1)
    start_time = time.time()
    str_result_1, str_result_2 = par_map_timeout_2(
        lambda: short_running_str("test 1", sleep_seconds=3),
        lambda: short_running_str("test 2", sleep_seconds=3),
        executor=executor,
        timeout=timedelta(seconds=4),
    )
    end_time = time.time()
    total_time = end_time - start_time
    assert total_time < 5, "The parmap should have timed out after 4 seconds"
    assert str_result_1 == "test 1"
    assert str_result_2 is None


def test_timeout_overall_ms():
    # The timeout should be applied overall
    # We limit the timeout to 40 ms
    # Each function takes 30 ms
    # So the parmap should timeout after 40 ms, not 80

    executor = ThreadPoolExecutor(1)
    start_time = time.time()
    str_result_1, str_result_2 = par_map_timeout_2(
        lambda: short_running_str("test 1", sleep_seconds=0.03),
        lambda: short_running_str("test 2", sleep_seconds=0.03),
        executor=executor,
        timeout=timedelta(milliseconds=40),
    )
    end_time = time.time()
    total_time = end_time - start_time
    assert total_time < 0.05, "The parmap should have timed out after 4 ms"
    assert str_result_1 == "test 1"
    assert str_result_2 is None

def test_timeout_overall():
    # The timeout should be applied to each function
    # We limit the timeout to 5 seconds
    # But supply it with 10 functions that take 1 second each
    # It should timeout after 5 seconds
    executor = ThreadPoolExecutor(1)
    start_time = time.time()
    par_map_timeout_n(
        lambda: short_running_str("test 1"),
        lambda: short_running_str("test 2"),
        lambda: short_running_str("test 3"),
        lambda: short_running_str("test 4"),
        lambda: short_running_str("test 5"),
        lambda: short_running_str("test 6"),
        lambda: short_running_str("test 7"),
        lambda: short_running_str("test 8"),
        lambda: short_running_str("test 9"),
        lambda: short_running_str("test 10"),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    end_time = time.time()
    total_time = end_time - start_time
    assert total_time < 6, "The parmap should have timed out after 5 seconds"
    assert total_time > 4, "The parmap should have timed out after 5 seconds"
