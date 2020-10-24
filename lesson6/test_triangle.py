from figure import Triangle
from math import isclose
import pytest


def get_triangle_area(a, b, c):
    p = get_triangle_perimeter(a, b, c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def get_triangle_perimeter(a, b, c):
    return a + b + c


def test_triangle_init():
    name = 'MyTest'
    a, b, c = 2, 3, 4
    t = Triangle(name, a, b, c)
    assert t.name == name
    assert t.a == a
    assert t.b == b
    assert t.c == c


def test_triangle_area():
    name = 'MyTest'
    sides = 2, 3, 4
    s = get_triangle_area(*sides)
    t = Triangle(name, *sides)
    assert isclose(s, t.area)


def test_triangle_perimeter():
    name = 'MyTest'
    sides = 2, 3, 4
    p = get_triangle_perimeter(*sides)
    t = Triangle(name, *sides)
    assert isclose(p, t.perimeter)


def test_add_triangle():
    name_1 = 'MyTest1'
    sides_1 = 2, 3, 4
    name_2 = 'MyTest2'
    sides_2 = 5, 6, 7
    s1 = get_triangle_area(*sides_1)
    s2 = get_triangle_area(*sides_2)
    t1 = Triangle(name_1, *sides_1)
    t2 = Triangle(name_2, *sides_2)
    assert isclose(t1.add_area(t2), s1 + s2)


def test_add_triangle_negative():
    name_1 = 'MyTest1'
    sides_1 = 2, 3, 4
    t1 = Triangle(name_1, *sides_1)
    with pytest.raises(TypeError):
        t1.add_area(123)
