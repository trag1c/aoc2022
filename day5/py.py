from samarium.python import export


@export
def parse_move(string: str) -> list[int]:
    return list(map(int, filter(str.isdigit, string.split())))


@export
def parse_stacks(data: str) -> list[str]:
    return [
        "".join(line[::-1][1:]).strip()
        for line in zip(*data.splitlines())
        if line[-1].isdigit()
    ]
