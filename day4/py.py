from samarium.python import export

@export
def parse_string(string: str) -> dict[str, int]:
    vals = [int(j) for i in string.split(",") for j in i.split("-")]
    return {i: j for i, j in zip(("1a", "1b", "2a", "2b"), vals)}
