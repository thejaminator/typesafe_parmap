import concurrent
from concurrent.futures import Future
from datetime import timedelta
from typing import Optional, Callable, Tuple

from typesafe_parmap.parmap import A1, A2


def try_future_result(
    future: concurrent.futures.Future[A1],
    timeout_seconds: float,
    logger: Optional[Callable[[str], None]],
    func_name: str,
) -> Optional[A1]:
    try:
        return future.result(timeout=timeout_seconds)
    except concurrent.futures.TimeoutError:
        if logger:
            logger(f"{func_name} timed out after {timeout_seconds} seconds")
        return None


def par_map_2_timeout(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2]]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    timeout_seconds = timeout.total_seconds()
    func_name_1 = func1.__name__
    func_name_2 = func2.__name__
    fut1_result = try_future_result(future=fut1, timeout_seconds=timeout_seconds, logger=logger, func_name=func_name_1)
    fut2_result = try_future_result(future=fut2, timeout_seconds=timeout_seconds, logger=logger, func_name=func_name_2)
    return fut1_result, fut2_result
