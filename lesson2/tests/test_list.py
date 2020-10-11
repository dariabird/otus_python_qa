import pytest


def test_append():
    l = [1, 2, 3]
    el_to_append = 4
    l.append(el_to_append)
    assert l[-1] == el_to_append, f"Wrong element appended. Actual: {l[-1]}. Expected: {el_to_append}"


def test_clear():
    l = [1, 2, 3]
    l.clear()
    assert len(l) == 0, "List was not cleared."


@pytest.mark.parametrize("l, el, count", [
    ([1, 2, 3], 1, 1),
    ([1, 2, 3, 3], 3, 2),
    (["a", "a", 2, 3, "a"], "a", 3),
    ([1, 2, 3], 4, 0),
])
def test_count(l, el, count):
    assert l.count(el) == count, f"Wrong count of given element. Actual {l.count(el)}. Expected: {count}"


def test_insert():
    l = [1, 3, 4]
    index, element = 1, 2
    l.insert(index, element)
    assert l[index] == element, f"Wrong insert operation. Expected element {element} at index {index}, " \
                                f"but got {l[index]}"


def test_extend():
    l1 = [1, 2, 3]
    len1 = len(l1)
    l2 = [4, 5, 6]
    l1.extend(l2)
    assert l1[len1:] == l2, "First array extension was wrong"
