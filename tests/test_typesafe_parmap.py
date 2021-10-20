#!/usr/bin/env python
"""Tests for `typesafe_parmap` package."""
import time
from concurrent.futures import ThreadPoolExecutor

from typesafe_parmap.parmap import par_map_3, par_map_2


def test_par_map() -> None:
    tp = ThreadPoolExecutor(5)
    first, second, third = par_map_3(lambda: 1, lambda: "qweq", lambda: 1.1, executor=tp)
    assert isinstance(first, int)
    assert isinstance(second, str)
    assert isinstance(third, float)


def test_example() -> None:
    tp = ThreadPoolExecutor(5)

    def long_running_int(param: int) -> int:
        time.sleep(5)  # long IO task here
        return 123

    def long_running_str(param: str) -> str:
        time.sleep(5)  # long IO task here
        return "hello world"

    int_result, str_result = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=tp)
    assert int_result == 123, str_result == "hello world"  # should finish in 5 seconds
