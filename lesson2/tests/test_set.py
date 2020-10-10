import pytest


def test_add():
    s = {1, 2, 3}
    el_to_add = 4
    s.add(el_to_add)
    assert el_to_add in s


def test_clear():
    s = {1, 2, 3}
    s.clear()
    assert s == set()


def test_discard():
    s = {1, 2, "a"}
    s.discard("a")
    assert "a" not in s


@pytest.mark.parametrize("s1, s2, expected", [
    ({1, "a", 3}, {2, "b", 3}, {'a', 1, 2, 3, 'b'}),
    ({1}, {"b"}, {1, "b"}),
])
def test_union(s1, s2, expected):
    assert s1.union(s2) == expected


@pytest.mark.parametrize("s1, s2, expected", [
    ({1, "a", 3}, {2, "b", 3}, {3}),
    ({1}, {"b"}, set()),
])
def test_intersection(s1, s2, expected):
    assert s1.intersection(s2) == expected
