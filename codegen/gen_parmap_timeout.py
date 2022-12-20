from codegen.constants import MAX_N


def generate_generics_assignments(n: int) -> str:
    generics: list[str] = []
    for i in range(1, n):
        generics.append(f'A{i} = TypeVar("A{i}")')
    return "\n".join(generics)


def generate_parmap(n: int) -> str:
    return f"""
def par_map_timeout_{n}(
    {signature_variables(n)},
    executor: concurrent.futures.Executor,
    timeout: timedelta,
    logger: Optional[Callable[[str], None]] = None,
) -> Tuple[{signature_return_generics(n)}]:
    {assignments(n)}
    return {return_statement(n)}
"""


def signature_variables(n: int) -> str:
    func_variables: list[str] = []
    for i in range(1, n + 1):
        func_variables.append(f"func{i}: Callable[[], A{i}]")
    return ",".join(func_variables)


def signature_return_generics(n: int) -> str:
    generics: list[str] = []
    for i in range(1, n + 1):
        generics.append(f"Optional[A{i}]")
    return ",".join(generics)


def assignments(n: int) -> str:
    var_assignments: list[str] = []
    var_assignments.append("starting_time = datetime.now()")
    var_assignments.append("time_left_after_fut0 = timeout")
    for i in range(1, n + 1):
        """
        executor.submit(func1)
        """
        var_assignments.append(f"fut{i} = executor.submit(func{i})")
    for i in range(1, n + 1):
        """
        fut1_result = try_future_result(
        future=fut1, timeout_left=time_left_after_fut0, overall_timeout=timeout, logger=logger, func_name=func1.__name__, func_number=1
        )
        """
        var_assignments.append(
            f"fut{i}_result = try_future_result(future=fut{i}, timeout_left=time_left_after_fut{i -1}, overall_timeout=timeout, logger=logger, func_name=func{i}.__name__, func_number={i})"
        )
        """
        time_left_after_fut1: timedelta = abs(timeout - (datetime.now() - starting_time))
        """
        var_assignments.append(f"time_left_after_fut{i}: timedelta = abs(timeout - (datetime.now() - starting_time))")

    return "\n    ".join(var_assignments)  # hacky indent


def return_statement(n: int) -> str:
    var_assignments: list[str] = []
    for i in range(1, n + 1):
        var_assignments.append(f"fut{i}_result")
    return ",".join(var_assignments)


if __name__ == "__main__":
    _parmap_funcs: list[str] = []
    for n in range(2, MAX_N):
        _parmap_funcs.append(generate_parmap(n))
    parmap_funcs = "\n".join(_parmap_funcs)
    generated = f"""
{generate_generics_assignments(MAX_N)}

{parmap_funcs}
"""
    with open("generated_gen_parmap_timeout.py", "w+") as text_file:
        text_file.write(generated)
