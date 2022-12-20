import concurrent
from concurrent.futures import Future
from datetime import timedelta, datetime
from typing import Optional, Callable, Tuple, TypeVar

A = TypeVar("A")


def min_zero_timedelta(td: timedelta) -> timedelta:
    # Ensure that the timedelta is not negative
    return max(timedelta(seconds=0), td)


def try_future_result(
    future: "concurrent.futures.Future[A]",
    timeout_left: timedelta,
    overall_timeout: timedelta,
    logger: Optional[Callable[[str], None]],
    func_name: str,
    func_number: int,
) -> Optional[A]:
    seconds_left = timeout_left.seconds
    overall_seconds = overall_timeout.seconds

    try:
        # Use the seconds_left as the timeout for the future result, not the overall timeout
        # This is so that the par_map timeout overall, not for each individual future
        return future.result(timeout=seconds_left)
    except concurrent.futures.TimeoutError:
        if logger:
            logger(f"par_map func{func_number}: {func_name} timed out after {overall_seconds} seconds")
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


def par_map_timeout_2(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result


def par_map_timeout_3(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result


def par_map_timeout_4(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result, fut4_result


def par_map_timeout_5(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result


def par_map_timeout_6(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result


def par_map_timeout_7(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7]]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result, fut7_result


def par_map_timeout_8(
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
    logger: Optional[Callable[[str], None]] = print,
) -> Tuple[
    Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7], Optional[A8]
]:
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut1_result = try_future_result(
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    return fut1_result, fut2_result, fut3_result, fut4_result, fut5_result, fut6_result, fut7_result, fut8_result


def par_map_timeout_9(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_10(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_11(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_12(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_13(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_14(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_15(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_16(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_17(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_18(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut18_result = try_future_result(
        future=fut18,
        timeout_left=time_left_after_fut17,
        overall_timeout=timeout,
        logger=logger,
        func_name=func18.__name__,
        func_number=18,
    )
    time_left_after_fut18: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_19(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut18_result = try_future_result(
        future=fut18,
        timeout_left=time_left_after_fut17,
        overall_timeout=timeout,
        logger=logger,
        func_name=func18.__name__,
        func_number=18,
    )
    time_left_after_fut18: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut19_result = try_future_result(
        future=fut19,
        timeout_left=time_left_after_fut18,
        overall_timeout=timeout,
        logger=logger,
        func_name=func19.__name__,
        func_number=19,
    )
    time_left_after_fut19: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_20(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut18_result = try_future_result(
        future=fut18,
        timeout_left=time_left_after_fut17,
        overall_timeout=timeout,
        logger=logger,
        func_name=func18.__name__,
        func_number=18,
    )
    time_left_after_fut18: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut19_result = try_future_result(
        future=fut19,
        timeout_left=time_left_after_fut18,
        overall_timeout=timeout,
        logger=logger,
        func_name=func19.__name__,
        func_number=19,
    )
    time_left_after_fut19: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut20_result = try_future_result(
        future=fut20,
        timeout_left=time_left_after_fut19,
        overall_timeout=timeout,
        logger=logger,
        func_name=func20.__name__,
        func_number=20,
    )
    time_left_after_fut20: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_21(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut18_result = try_future_result(
        future=fut18,
        timeout_left=time_left_after_fut17,
        overall_timeout=timeout,
        logger=logger,
        func_name=func18.__name__,
        func_number=18,
    )
    time_left_after_fut18: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut19_result = try_future_result(
        future=fut19,
        timeout_left=time_left_after_fut18,
        overall_timeout=timeout,
        logger=logger,
        func_name=func19.__name__,
        func_number=19,
    )
    time_left_after_fut19: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut20_result = try_future_result(
        future=fut20,
        timeout_left=time_left_after_fut19,
        overall_timeout=timeout,
        logger=logger,
        func_name=func20.__name__,
        func_number=20,
    )
    time_left_after_fut20: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut21_result = try_future_result(
        future=fut21,
        timeout_left=time_left_after_fut20,
        overall_timeout=timeout,
        logger=logger,
        func_name=func21.__name__,
        func_number=21,
    )
    time_left_after_fut21: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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


def par_map_timeout_22(
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
    logger: Optional[Callable[[str], None]] = print,
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
    starting_time = datetime.now()
    time_left_after_fut0 = timeout
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
        future=fut1,
        timeout_left=time_left_after_fut0,
        overall_timeout=timeout,
        logger=logger,
        func_name=func1.__name__,
        func_number=1,
    )
    time_left_after_fut1: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut2_result = try_future_result(
        future=fut2,
        timeout_left=time_left_after_fut1,
        overall_timeout=timeout,
        logger=logger,
        func_name=func2.__name__,
        func_number=2,
    )
    time_left_after_fut2: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut3_result = try_future_result(
        future=fut3,
        timeout_left=time_left_after_fut2,
        overall_timeout=timeout,
        logger=logger,
        func_name=func3.__name__,
        func_number=3,
    )
    time_left_after_fut3: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut4_result = try_future_result(
        future=fut4,
        timeout_left=time_left_after_fut3,
        overall_timeout=timeout,
        logger=logger,
        func_name=func4.__name__,
        func_number=4,
    )
    time_left_after_fut4: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut5_result = try_future_result(
        future=fut5,
        timeout_left=time_left_after_fut4,
        overall_timeout=timeout,
        logger=logger,
        func_name=func5.__name__,
        func_number=5,
    )
    time_left_after_fut5: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut6_result = try_future_result(
        future=fut6,
        timeout_left=time_left_after_fut5,
        overall_timeout=timeout,
        logger=logger,
        func_name=func6.__name__,
        func_number=6,
    )
    time_left_after_fut6: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut7_result = try_future_result(
        future=fut7,
        timeout_left=time_left_after_fut6,
        overall_timeout=timeout,
        logger=logger,
        func_name=func7.__name__,
        func_number=7,
    )
    time_left_after_fut7: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut8_result = try_future_result(
        future=fut8,
        timeout_left=time_left_after_fut7,
        overall_timeout=timeout,
        logger=logger,
        func_name=func8.__name__,
        func_number=8,
    )
    time_left_after_fut8: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut9_result = try_future_result(
        future=fut9,
        timeout_left=time_left_after_fut8,
        overall_timeout=timeout,
        logger=logger,
        func_name=func9.__name__,
        func_number=9,
    )
    time_left_after_fut9: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut10_result = try_future_result(
        future=fut10,
        timeout_left=time_left_after_fut9,
        overall_timeout=timeout,
        logger=logger,
        func_name=func10.__name__,
        func_number=10,
    )
    time_left_after_fut10: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut11_result = try_future_result(
        future=fut11,
        timeout_left=time_left_after_fut10,
        overall_timeout=timeout,
        logger=logger,
        func_name=func11.__name__,
        func_number=11,
    )
    time_left_after_fut11: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut12_result = try_future_result(
        future=fut12,
        timeout_left=time_left_after_fut11,
        overall_timeout=timeout,
        logger=logger,
        func_name=func12.__name__,
        func_number=12,
    )
    time_left_after_fut12: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut13_result = try_future_result(
        future=fut13,
        timeout_left=time_left_after_fut12,
        overall_timeout=timeout,
        logger=logger,
        func_name=func13.__name__,
        func_number=13,
    )
    time_left_after_fut13: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut14_result = try_future_result(
        future=fut14,
        timeout_left=time_left_after_fut13,
        overall_timeout=timeout,
        logger=logger,
        func_name=func14.__name__,
        func_number=14,
    )
    time_left_after_fut14: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut15_result = try_future_result(
        future=fut15,
        timeout_left=time_left_after_fut14,
        overall_timeout=timeout,
        logger=logger,
        func_name=func15.__name__,
        func_number=15,
    )
    time_left_after_fut15: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut16_result = try_future_result(
        future=fut16,
        timeout_left=time_left_after_fut15,
        overall_timeout=timeout,
        logger=logger,
        func_name=func16.__name__,
        func_number=16,
    )
    time_left_after_fut16: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut17_result = try_future_result(
        future=fut17,
        timeout_left=time_left_after_fut16,
        overall_timeout=timeout,
        logger=logger,
        func_name=func17.__name__,
        func_number=17,
    )
    time_left_after_fut17: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut18_result = try_future_result(
        future=fut18,
        timeout_left=time_left_after_fut17,
        overall_timeout=timeout,
        logger=logger,
        func_name=func18.__name__,
        func_number=18,
    )
    time_left_after_fut18: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut19_result = try_future_result(
        future=fut19,
        timeout_left=time_left_after_fut18,
        overall_timeout=timeout,
        logger=logger,
        func_name=func19.__name__,
        func_number=19,
    )
    time_left_after_fut19: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut20_result = try_future_result(
        future=fut20,
        timeout_left=time_left_after_fut19,
        overall_timeout=timeout,
        logger=logger,
        func_name=func20.__name__,
        func_number=20,
    )
    time_left_after_fut20: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut21_result = try_future_result(
        future=fut21,
        timeout_left=time_left_after_fut20,
        overall_timeout=timeout,
        logger=logger,
        func_name=func21.__name__,
        func_number=21,
    )
    time_left_after_fut21: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
    fut22_result = try_future_result(
        future=fut22,
        timeout_left=time_left_after_fut21,
        overall_timeout=timeout,
        logger=logger,
        func_name=func22.__name__,
        func_number=22,
    )
    time_left_after_fut22: timedelta = min_zero_timedelta(timeout - (datetime.now() - starting_time))
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
