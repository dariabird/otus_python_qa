import pytest


@pytest.mark.parametrize("s, sub, count", [
    ("my_string", "str", 1),
    ("my_string", "test", 0),
])
def test_count(s, sub, count):
    assert s.count(sub) == count, "Wrong count of substring in string."


@pytest.mark.parametrize("s, end, expected", [
    ("my_string", "ing", True),
    ("my_string", "test", False),
])
def test_endswith(s, end, expected):
    assert s.endswith(end) is expected


@pytest.mark.parametrize("s, sub, expected", [
    ("my_string", "str", 3),
    ("my_string", "test", -1),
])
def test_find(s, sub, expected):
    assert s.find(sub) == expected


@pytest.mark.parametrize("s, expected", [
    ("test", True),
    ("", False),
    ("a123a", False),
])
def test_isalpha(s, expected):
    assert s.isalpha() is expected


@pytest.mark.parametrize("s, sep, expected", [
    ("1,2,3", ",", ["1", "2", "3"]),
    ("1 2 3", None, ["1", "2", "3"]),
    ("1,2,3", " ", ["1,2,3"]),
])
def test_split(s, sep, expected):
    assert s.split(sep) == expected
