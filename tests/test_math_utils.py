from genai_scaffolding_pro.math_utils import add, bad_add


def test_add():
    assert add(2, 3) == 5


def test_bad_add():
    # This one will "work" at runtime but mypy will complain
    assert bad_add(2, 3) == "5"
