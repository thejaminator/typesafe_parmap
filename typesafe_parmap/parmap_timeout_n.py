from typing import overload, Union
from concurrent.futures import Future
from typesafe_parmap.parmap_timeout import *


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7]]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    *,
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[
    Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7], Optional[A8]
]:
    ...


@overload
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


@overload
def par_map_timeout_n(
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
    *,
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
    ...


def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Optional[Callable[[], A3]] = None,
    func4: Optional[Callable[[], A4]] = None,
    func5: Optional[Callable[[], A5]] = None,
    func6: Optional[Callable[[], A6]] = None,
    func7: Optional[Callable[[], A7]] = None,
    func8: Optional[Callable[[], A8]] = None,
    func9: Optional[Callable[[], A9]] = None,
    func10: Optional[Callable[[], A10]] = None,
    func11: Optional[Callable[[], A11]] = None,
    func12: Optional[Callable[[], A12]] = None,
    func13: Optional[Callable[[], A13]] = None,
    func14: Optional[Callable[[], A14]] = None,
    func15: Optional[Callable[[], A15]] = None,
    func16: Optional[Callable[[], A16]] = None,
    func17: Optional[Callable[[], A17]] = None,
    func18: Optional[Callable[[], A18]] = None,
    func19: Optional[Callable[[], A19]] = None,
    func20: Optional[Callable[[], A20]] = None,
    func21: Optional[Callable[[], A21]] = None,
    func22: Optional[Callable[[], A22]] = None,
    *,  # Makes executor, timeout, and logger keyword only
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Union[
    Tuple[Optional[A1], Optional[A2]],
    Tuple[Optional[A1], Optional[A2], Optional[A3]],
    Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4]],
    Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5]],
    Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6]],
    Tuple[Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7]],
    Tuple[
        Optional[A1], Optional[A2], Optional[A3], Optional[A4], Optional[A5], Optional[A6], Optional[A7], Optional[A8]
    ],
    Tuple[
        Optional[A1],
        Optional[A2],
        Optional[A3],
        Optional[A4],
        Optional[A5],
        Optional[A6],
        Optional[A7],
        Optional[A8],
        Optional[A9],
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
    Tuple[
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
    ],
]:
    """Executes 2 to 22 functions in parallel"""
    if (
        func22 is not None
        and func21 is not None
        and func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_22(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            func21=func21,
            func22=func22,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func21 is not None
        and func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_21(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            func21=func21,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_20(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_19(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_18(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_17(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_16(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_15(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_14(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_13(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_12(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_11(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_10(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_9(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if (
        func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_timeout_8(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if func7 is not None and func6 is not None and func5 is not None and func4 is not None and func3 is not None:
        return par_map_timeout_7(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if func6 is not None and func5 is not None and func4 is not None and func3 is not None:
        return par_map_timeout_6(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if func5 is not None and func4 is not None and func3 is not None:
        return par_map_timeout_5(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            executor=executor,
            timeout=timeout,
            logger=logger,
        )
    if func4 is not None and func3 is not None:
        return par_map_timeout_4(
            func1=func1, func2=func2, func3=func3, func4=func4, executor=executor, timeout=timeout, logger=logger
        )
    if func3 is not None:
        return par_map_timeout_3(
            func1=func1, func2=func2, func3=func3, executor=executor, timeout=timeout, logger=logger
        )
    else:
        return par_map_timeout_2(func1=func1, func2=func2, executor=executor, timeout=timeout, logger=logger)
