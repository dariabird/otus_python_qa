import pytest


@pytest.mark.parametrize("d, k, default, expected", [
    ({"a": 1, "b": 2}, "b", None, 2),
    ({"a": 1, "b": 2}, "c", 3, 3),
    ({"a": 1, "b": 2}, "c", None, None),
])
def test_get(d, k, default, expected):
    assert d.get(k, default) == expected


def test_clear():
    d = {"a": 1, "b": 2}
    d.clear()
    assert d == dict()


def test_pop_ok():
    d = {"a": 1, "b": 2}
    assert d.pop("a") == 1


def test_pop_with_default():
    d = {"a": 1, "b": 2}
    assert d.pop("c", 3) == 3


def test_pop_exception():
    d = {"a": 1, "b": 2}
    with pytest.raises(KeyError):
        d.pop("c")


