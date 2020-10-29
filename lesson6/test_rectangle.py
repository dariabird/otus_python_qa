from figure import Rectangle
from math import isclose
import pytest


def test_rectangle_init():
    name = 'MyTest'
    a, b = 2, 4
    r = Rectangle(name, a, b)
    assert r.name == name
    assert r.a == a
    assert r.b == b


def test_rectangle_area():
    name = 'MyTest'
    a, b = 2, 3
    s = a * b
    r = Rectangle(name, a, b)
    assert isclose(s, r.area)


def test_rectangle_perimeter():
    name = 'MyTest'
    a, b = 2, 4
    p = (a + b) * 2
    r = Rectangle(name, a, b)
    assert isclose(p, r.perimeter)


def test_add_rectangle():
    name_1 = 'MyTest1'
    a, b = 2, 4
    name_2 = 'MyTest2'
    c, d = 4, 7
    s1 = a * b
    s2 = c * d
    r1 = Rectangle(name_1, a, b)
    r2 = Rectangle(name_2, c, d)
    assert isclose(r1.add_area(r2), s1 + s2)


def test_add_rectangle_negative():
    name_1 = 'MyTest1'
    a, b = 2, 4
    r1 = Rectangle(name_1, a, b)
    with pytest.raises(TypeError):
        r1.add_area(123)
