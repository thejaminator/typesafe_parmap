from codegen.constants import MAX_N


def generate_generics_assignments(n: int) -> str:
    generics: list[str] = []
    for i in range(1, n):
        generics.append(f'A{i} = TypeVar("A{i}")')
    return "\n".join(generics)


def generate_parmap(n: int) -> str:
    return f"""
def par_map_{n}(
    {signature_variables(n)},
    executor: concurrent.futures.Executor,
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
        generics.append(f"A{i}")
    return ",".join(generics)


def assignments(n: int) -> str:
    var_assignments: list[str] = []
    for i in range(1, n + 1):
        var_assignments.append(f"fut{i} = executor.submit(func{i})")
    return "\n    ".join(var_assignments)  # hacky indent


def return_statement(n: int) -> str:
    var_assignments: list[str] = []
    for i in range(1, n + 1):
        var_assignments.append(f"fut{i}.result()")
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
    with open("generated.py", "w+") as text_file:
        text_file.write(generated)
