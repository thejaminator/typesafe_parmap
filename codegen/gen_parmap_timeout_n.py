from codegen.constants import MAX_N
from codegen.gen_parmap_timeout import signature_return_generics

# To generate the actual function
def generate_parmap_n_main_fn() -> str:
    return f"""
def par_map_timeout_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    {optional_signature_variables(start=3, n=MAX_N)},
    *, # Makes executor, timeout, and logger keyword only
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Union[{tuple_returns()}]:
    \"""Executes 2 to 22 functions in parallel\"""
    {all_checks_and_returns()}
    else:
        return par_map_timeout_2(func1=func1, func2=func2, executor=executor, timeout=timeout, logger=logger)
"""


def optional_signature_variables(start: int, n: int) -> str:
    func_variables: list[str] = []
    for i in range(start, n):
        func_variables.append(f"func{i}: Optional[Callable[[], A{i}]] = None")
    return ",".join(func_variables)


def tuple_returns() -> str:
    tuples: list[str] = []
    for i in range(2, MAX_N):
        tuples.append(f"Tuple[{signature_return_generics(i)}]")
    return ",".join(tuples)


def is_not_none_checks(n: int) -> str:
    predicates: list[str] = []
    for i in range(n, 2, -1):  # stop at 2 because don't need to check func2 and fun1
        predicates.append(f"func{i} is not None")
    joined_preds = " and ".join(predicates)
    return f"if {joined_preds}:"


def return_statement(n: int) -> str:
    return f"    return par_map_timeout_{n}({keyword_args(n)},executor=executor, timeout=timeout, logger=logger)"


def keyword_args(n: int) -> str:
    keywords: list[str] = []
    for i in range(1, n + 1):
        keywords.append(f"func{i}=func{i}")
    return ",".join(keywords)


def all_checks_and_returns() -> str:
    check_and_returns: list[str] = []
    for i in range(MAX_N - 1, 2, -1):
        check_and_returns.append(is_not_none_checks(i) + "\n    " + return_statement(i))
    return "\n    ".join(check_and_returns)


# end: To generate the actual function

# To generate the @overload hints


def generate_overloads() -> str:
    overloads: list[str] = []
    for i in range(2, MAX_N):
        overloads.append(generate_single_overload(i))
    return "\n".join(overloads)


def generate_single_overload(i: int) -> str:
    definition = f"""
@overload
def par_map_timeout_n({mandatory_signature_variables(i)}, *, executor: concurrent.futures.Executor, timeout: timedelta, logger: Optional[Callable[[str], None]] = None) -> Tuple[{signature_return_generics(i)}]:
    ...
"""
    return definition


def mandatory_signature_variables(n: int) -> str:
    func_variables: list[str] = []
    for i in range(1, n + 1):
        func_variables.append(f"func{i}: Callable[[], A{i}]")
    return ",".join(func_variables)


if __name__ == "__main__":
    overloads: str = generate_overloads()
    main_function: str = generate_parmap_n_main_fn()
    with open("generated_gen_parmap_timeout_n.py", "w+") as text_file:
        text_file.write(overloads)
        text_file.write(main_function)
