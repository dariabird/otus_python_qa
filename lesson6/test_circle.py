from figure import Circle
from math import isclose, pi
import pytest


def test_circle_init():
    name = 'MyTest'
    r = 5
    c = Circle(name, r)
    assert c.name == name
    assert c.r == r


def test_circle_area():
    name = 'MyTest'
    r = 6
    s = pi * r ** 2
    c = Circle(name, r)
    assert isclose(s, c.area)


def test_circle_perimeter():
    name = 'MyTest'
    r = 7
    p = 2 * pi * r
    c = Circle(name, r)
    assert isclose(p, c.perimeter)


def test_add_circle():
    name_1 = 'MyTest1'
    r1 = 4
    name_2 = 'MyTest2'
    r2 = 7
    s1 = pi * r1 ** 2
    s2 = pi * r2 ** 2
    c1 = Circle(name_1, r1)
    c2 = Circle(name_2, r2)
    assert isclose(c1.add_area(c2), s1 + s2)


def test_add_circle_negative():
    name_1 = 'MyTest1'
    r = 2.4
    c = Circle(name_1, r)
    with pytest.raises(TypeError):
        c.add_area(123)
