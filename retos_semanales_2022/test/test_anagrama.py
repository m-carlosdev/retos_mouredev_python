from retos.anagrama import isAnagram, text_formatter
import pytest

def test_text_fomatter():
    assert text_formatter("Dán,ger D'am/o.1") == "dangerdamo1"

@pytest.mark.parametrize(
    "string_1, string_2, expected",
    [
        ("Danger D'amo", "Armageddon", True),
        ("Hello World", "Hola mundo", False)
    ]
)
def test_isAnagram(string_1, string_2, expected):
    assert isAnagram(string_1, string_2) == expected
