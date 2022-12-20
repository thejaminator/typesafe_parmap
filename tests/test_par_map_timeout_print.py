from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

from tests.test_par_map_timeout_n import long_running_int, short_running_str
from typesafe_parmap import par_map_timeout_n, NamedThunk


def test_timeout_parmap_logger():
    executor = ThreadPoolExecutor(2)
    set_value: str = ""

    def fake_logger(string: str) -> None:
        nonlocal set_value
        set_value = string

    par_map_timeout_n(
        lambda: long_running_int(5),
        lambda: short_running_str("test 2"),
        executor=executor,
        timeout=timedelta(seconds=3),
        logger=fake_logger,
    )
    assert (
        set_value == "par_map func1: <lambda> timed out after 3.0 seconds"
    ), "The logger should have been called with the correct message"


def test_timeout_parmap_named_thunk():
    from typesafe_parmap import NamedThunk
    executor = ThreadPoolExecutor(2)
    set_value: str = ""

    def fake_logger(string: str) -> None:
        nonlocal set_value
        set_value = string

    par_map_timeout_n(
        NamedThunk(lambda: long_running_int(5), name="Long Running Int"),
        lambda: short_running_str("test 2"),
        executor=executor,
        timeout=timedelta(seconds=3),
        logger=fake_logger,
    )
    assert (
        set_value == "par_map func1: Long Running Int timed out after 3.0 seconds"
    ), "The logger should have been called with the correct message"

def test_timeout_parmap_named_thunk_example():
    executor = ThreadPoolExecutor(2)
    par_map_timeout_n(
        NamedThunk(lambda: long_running_int(5), name="Long Running Int"),
        lambda: short_running_str("test 2"),
        executor=executor,
        timeout=timedelta(seconds=3),
        logger=print,
    )
    # Prints:
    # par_map func1: Long Running Int timed out after 3.0 seconds
