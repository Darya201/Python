import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("sky", "Sky"),
        ("", ""),
        ],
    ids=["capitalize normal string", "capitalize empty string"]
    )
def test_capitalize_posistve(input_str, expected_output):
    assert string_utils.capitalize(input_str) == expected_output


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("SkyPro", "SkyPro"),
        ("123abc", "123abc"),
    ],
    ids=["already capitalized", "numbers first"]
)
def test_capitalize_negative(input_str, expected_output):
    assert string_utils.capitalize(input_str) != expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
    ],
    ids=["trim leading spaces", "no spaces to trim"]
    )
def test_trim_positive(input_str, expected_output):
    assert string_utils.trim(input_str) == expected_output


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("skypro   ", "skypro   "),
        (" s k y p r o ", "s k y p r o "),
    ],
    ids=["trailing spaces not removed", "inner spaces not removed"]
)
def test_trim_negative(input_str, expected_output):
    assert string_utils.trim(input_str) != expected_output


@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "y", True),
    ],
    ids=["contains 'S'", "contains 'y'"]
)
def test_contains_positive(string, symbol, expected_output):
    assert string_utils.contains(string, symbol) == expected_output


@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "U", False),
        ("", "x", False),
    ],
    ids=["does not contain 'U'", "empty string check"]
)
def test_contains_negative(string, symbol, expected_output):
    assert string_utils.contains(string, symbol) == expected_output


@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "k", "SyPro"),
        ("Hello World", "o", "Hell Wrld"),
    ],
    ids=["delete 'k'", "delete all 'o's"]
)
def test_delete_symbol_positive(string, symbol, expected_output):
    assert string_utils.delete_symbol(string, symbol) == expected_output


@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "Z", "SkyPro"),
        ("Hello", "ll", "Heo"),
    ],
    ids=["symbol not found", "substring deletion"]
)
def test_delete_symbol_negative(string, symbol, expected_output):
    assert string_utils.delete_symbol(string, symbol) != expected_output
