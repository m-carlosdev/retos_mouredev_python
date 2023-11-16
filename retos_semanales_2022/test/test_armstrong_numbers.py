from retos.armstrong_numbers import is_armstrong
import pytest


@pytest.mark.parametrize(
    "number, expected",
    [(371, True), (258, False), (8208, True), (4210818, True)]
)
def test_is_armstrong(number, expected):
    assert is_armstrong(number) == expected
