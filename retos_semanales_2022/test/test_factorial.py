from retos.factorial import factorial
import pytest

@pytest.mark.parametrize(
    "number, result",
    [(0, 1), (1, 1), (2, 2), (5, 120), (-1, 0), (13, 6227020800)]
)
def test_factorial(number, result):
    assert factorial(number) == result
