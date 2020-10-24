from figure import Square
from math import isclose
import pytest


def test_square_init():
    name = 'MyTest'
    a = 5
    s = Square(name, a)
    assert s.name == name
    assert s.a == a


def test_square_area():
    name = 'MyTest'
    a = 5
    s = Square(name, a)
    area = a ** 2
    assert isclose(area, s.area)


def test_square_perimeter():
    name = 'MyTest'
    a = 5
    s = Square(name, a)
    p = a * 4
    assert isclose(p, s.perimeter)


def test_add_square():
    name_1 = 'MyTest1'
    a1 = 4
    name_2 = 'MyTest2'
    a2 = 7
    area_1 = a1 ** 2
    area_2 = a2 ** 2
    s1 = Square(name_1, a1)
    s2 = Square(name_2, a2)
    assert isclose(s1.add_area(s2), area_1 + area_2)


def test_add_square_negative():
    name_1 = 'MyTest1'
    a = 2.4
    s = Square(name_1, a)
    with pytest.raises(TypeError):
        s.add_area(123)
