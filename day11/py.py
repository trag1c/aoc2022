from samarium.python import export


@export
def parse_string(
    string: str,
) -> tuple[list[int], tuple[str, str], int, tuple[int, int]]:
    _, si_base, op_base, test_base, *outcome_base = string.splitlines()
    starting_items = list(map(int, si_base.split(": ")[1].split(",")))
    op_frag = op_base.split("old ")[1]
    operator = op_frag[0]
    arg = op_frag[2:]
    test = int(test_base.split()[-1])
    true, false = [int(i.split("monkey ")[1]) for i in outcome_base]
    return starting_items, (operator, arg), test, (true, false)
