import concurrent
from concurrent.futures import Future
from datetime import timedelta
from typing import Optional, Callable, Tuple, TypeVar

A = TypeVar("A")


def try_future_result(
    future: concurrent.futures.Future[A],
    timeout: timedelta,
    logger: Optional[Callable[[str], None]],
    func_name: str,
    func_number: int,
) -> Optional[A]:
    seconds = timeout.seconds
    try:
        return future.result(timeout=seconds)
    except concurrent.futures.TimeoutError:
        if logger:
            logger(f"par_map func{func_number}: {func_name} timed out after {seconds} seconds")
        return None


A1 = TypeVar("A1")
A2 = TypeVar("A2")
A3 = TypeVar("A3")
A4 = TypeVar("A4")
A5 = TypeVar("A5")
A6 = TypeVar("A6")
A7 = TypeVar("A7")
A8 = TypeVar("A8")
A9 = TypeVar("A9")
A10 = TypeVar("A10")
A11 = TypeVar("A11")
A12 = TypeVar("A12")
A13 = TypeVar("A13")
A14 = TypeVar("A14")
A15 = TypeVar("A15")
A16 = TypeVar("A16")
A17 = TypeVar("A17")
A18 = TypeVar("A18")
A19 = TypeVar("A19")
A20 = TypeVar("A20")
A21 = TypeVar("A21")
A22 = TypeVar("A22")


def par_map_2_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    return fut1_result, fut2_result


def par_map_3_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    return fut1_result, fut2_result, fut3_result


def par_map_4_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    return fut1_result, fut2_result, fut3_result, fut4_result


def par_map_5_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result


def par_map_6_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result


def par_map_7_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result, fut7_result


def par_map_8_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7], Optional[A8]
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result, fut7_result, fut8_result


def par_map_9_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
    )


def par_map_10_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
    )


def par_map_11_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
    )


def par_map_12_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
    )


def par_map_13_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
    )


def par_map_14_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
    )


def par_map_15_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
    )


def par_map_16_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
    )


def par_map_17_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
    )


def par_map_18_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
    Optional[A18],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    fut18_result = try_future_result(
        future=fut18, timeout=timeout, logger=logger, func_name=func18.__name__, func_number=18
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
        fut18_result,
    )


def par_map_19_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
    Optional[A18],
    Optional[A19],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    fut18_result = try_future_result(
        future=fut18, timeout=timeout, logger=logger, func_name=func18.__name__, func_number=18
    )
    fut19_result = try_future_result(
        future=fut19, timeout=timeout, logger=logger, func_name=func19.__name__, func_number=19
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
        fut18_result,
        fut19_result,
    )


def par_map_20_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
    Optional[A18],
    Optional[A19],
    Optional[A20],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    fut18_result = try_future_result(
        future=fut18, timeout=timeout, logger=logger, func_name=func18.__name__, func_number=18
    )
    fut19_result = try_future_result(
        future=fut19, timeout=timeout, logger=logger, func_name=func19.__name__, func_number=19
    )
    fut20_result = try_future_result(
        future=fut20, timeout=timeout, logger=logger, func_name=func20.__name__, func_number=20
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
        fut18_result,
        fut19_result,
        fut20_result,
    )


def par_map_21_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
    Optional[A18],
    Optional[A19],
    Optional[A20],
    Optional[A21],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    fut21 = executor.submit(func21)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    fut18_result = try_future_result(
        future=fut18, timeout=timeout, logger=logger, func_name=func18.__name__, func_number=18
    )
    fut19_result = try_future_result(
        future=fut19, timeout=timeout, logger=logger, func_name=func19.__name__, func_number=19
    )
    fut20_result = try_future_result(
        future=fut20, timeout=timeout, logger=logger, func_name=func20.__name__, func_number=20
    )
    fut21_result = try_future_result(
        future=fut21, timeout=timeout, logger=logger, func_name=func21.__name__, func_number=21
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
        fut18_result,
        fut19_result,
        fut20_result,
        fut21_result,
    )


def par_map_22_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    func22: Callable[[], A22],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1],
    Optional[A2],
    Optional[A3],
    Optional[A4],
    Optional[A5],
    Optional[A6],
    Optional[A7],
    Optional[A8],
    Optional[A9],
    Optional[A10],
    Optional[A11],
    Optional[A12],
    Optional[A13],
    Optional[A14],
    Optional[A15],
    Optional[A16],
    Optional[A17],
    Optional[A18],
    Optional[A19],
    Optional[A20],
    Optional[A21],
    Optional[A22],
]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    fut21 = executor.submit(func21)
    fut22 = executor.submit(func22)
    fut1_result = try_future_result(
        future=fut1, timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
    )
    fut2_result = try_future_result(
        future=fut2, timeout=timeout, logger=logger, func_name=func2.__name__, func_number=2
    )
    fut3_result = try_future_result(
        future=fut3, timeout=timeout, logger=logger, func_name=func3.__name__, func_number=3
    )
    fut4_result = try_future_result(
        future=fut4, timeout=timeout, logger=logger, func_name=func4.__name__, func_number=4
    )
    fut5_result = try_future_result(
        future=fut5, timeout=timeout, logger=logger, func_name=func5.__name__, func_number=5
    )
    fut6_result = try_future_result(
        future=fut6, timeout=timeout, logger=logger, func_name=func6.__name__, func_number=6
    )
    fut7_result = try_future_result(
        future=fut7, timeout=timeout, logger=logger, func_name=func7.__name__, func_number=7
    )
    fut8_result = try_future_result(
        future=fut8, timeout=timeout, logger=logger, func_name=func8.__name__, func_number=8
    )
    fut9_result = try_future_result(
        future=fut9, timeout=timeout, logger=logger, func_name=func9.__name__, func_number=9
    )
    fut10_result = try_future_result(
        future=fut10, timeout=timeout, logger=logger, func_name=func10.__name__, func_number=10
    )
    fut11_result = try_future_result(
        future=fut11, timeout=timeout, logger=logger, func_name=func11.__name__, func_number=11
    )
    fut12_result = try_future_result(
        future=fut12, timeout=timeout, logger=logger, func_name=func12.__name__, func_number=12
    )
    fut13_result = try_future_result(
        future=fut13, timeout=timeout, logger=logger, func_name=func13.__name__, func_number=13
    )
    fut14_result = try_future_result(
        future=fut14, timeout=timeout, logger=logger, func_name=func14.__name__, func_number=14
    )
    fut15_result = try_future_result(
        future=fut15, timeout=timeout, logger=logger, func_name=func15.__name__, func_number=15
    )
    fut16_result = try_future_result(
        future=fut16, timeout=timeout, logger=logger, func_name=func16.__name__, func_number=16
    )
    fut17_result = try_future_result(
        future=fut17, timeout=timeout, logger=logger, func_name=func17.__name__, func_number=17
    )
    fut18_result = try_future_result(
        future=fut18, timeout=timeout, logger=logger, func_name=func18.__name__, func_number=18
    )
    fut19_result = try_future_result(
        future=fut19, timeout=timeout, logger=logger, func_name=func19.__name__, func_number=19
    )
    fut20_result = try_future_result(
        future=fut20, timeout=timeout, logger=logger, func_name=func20.__name__, func_number=20
    )
    fut21_result = try_future_result(
        future=fut21, timeout=timeout, logger=logger, func_name=func21.__name__, func_number=21
    )
    fut22_result = try_future_result(
        future=fut22, timeout=timeout, logger=logger, func_name=func22.__name__, func_number=22
    )
    return (
        fut1_result,
        fut2_result,
        fut3_result,
        fut4_result,
        fut5_result,
        fut6_result,
        fut7_result,
        fut8_result,
        fut9_result,
        fut10_result,
        fut11_result,
        fut12_result,
        fut13_result,
        fut14_result,
        fut15_result,
        fut16_result,
        fut17_result,
        fut18_result,
        fut19_result,
        fut20_result,
        fut21_result,
        fut22_result,
    )
