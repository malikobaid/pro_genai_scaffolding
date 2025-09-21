def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def bad_add(a, b):
    # deliberately sloppy code for Ruff + Mypy demo
    y = 123
    x = a + b
    return str(x)  # wrong type!
