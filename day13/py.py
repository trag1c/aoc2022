from samarium.python import export


@export
def evaluate(string: str) -> list[int]:
    assert isinstance(x := eval(string), list)
    return x
