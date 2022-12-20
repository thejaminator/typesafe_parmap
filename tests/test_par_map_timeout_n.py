import time
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

from typesafe_parmap.parmap_timeout import par_map_timeout_2
from typesafe_parmap.parmap_timeout_n import par_map_timeout_n


def long_running_int(param: int) -> int:
    time.sleep(10)  # long IO task here that should tiemout
    return param


def short_running_str(param: str) -> str:
    time.sleep(1)
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


def test_timeout_parmap_n():
    executor = ThreadPoolExecutor(2)
    int_result, str_result_1, str_result_2 = par_map_timeout_n(
        func1=lambda: long_running_int(5),
        func2=lambda: short_running_str("test 1"),
        func3=lambda: short_running_str("test 2"),
        executor=executor,
        timeout=timedelta(seconds=5),
    )
    assert int_result is None
    assert str_result_1 == "test 1"
    assert str_result_2 == "test 2"
