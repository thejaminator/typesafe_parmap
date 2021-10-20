#!/usr/bin/env python
"""Tests for `typesafe_parmap` package."""
from concurrent.futures import ThreadPoolExecutor

from typesafe_parmap.typesafe_parmap import par_map_3


def test_par_map() -> None:
    tp = ThreadPoolExecutor(5)
    first, second, third = par_map_3(lambda: 1, lambda: "qweq", lambda: 1.1, executor=tp)
    assert isinstance(first, int)
    assert isinstance(second, str)
    assert isinstance(third, str)
