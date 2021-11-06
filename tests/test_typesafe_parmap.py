#!/usr/bin/env python
"""Tests for `typesafe_parmap` package."""
import time
from concurrent.futures import ThreadPoolExecutor

from typesafe_parmap import par_map_2, par_map_3, par_map_n


tp = ThreadPoolExecutor(5)


def test_par_map() -> None:
    first, second, third = par_map_3(lambda: 1, lambda: "qweq", lambda: 1.1, executor=tp)
    assert isinstance(first, int)
    assert isinstance(second, str)
    assert isinstance(third, float)


def test_par_map_n() -> None:
    assert par_map_3(lambda: 1, lambda: "qweq", lambda: 1.1, executor=tp) == par_map_n(
        lambda: 1, lambda: "qweq", lambda: 1.1, executor=tp
    )
    assert par_map_2(lambda: 1, lambda: "qweq", executor=tp) == par_map_n(lambda: 1, lambda: "qweq", executor=tp)


def test_example() -> None:
    executor = ThreadPoolExecutor(5)

    def long_running_int(param: int) -> int:
        time.sleep(1)  # long IO task here
        return 123

    def long_running_str(param: str) -> str:
        time.sleep(1)  # long IO task here
        return "hello world"

    int_result, str_result = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)
    assert int_result == 123, str_result == "hello world"  # should finish in 5 seconds

    a = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)
    b = par_map_n(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)

    assert a == b

    c = par_map_3(
        lambda: long_running_int(5),
        lambda: long_running_str("test"),
        lambda: long_running_str("test"),
        executor=executor,
    )
    d = par_map_n(
        lambda: long_running_int(5),
        lambda: long_running_str("test"),
        lambda: long_running_str("test"),
        executor=executor,
    )

    assert c == d
