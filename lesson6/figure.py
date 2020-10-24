from abc import abstractmethod
from math import pi


class Figure:
    name = None
    __angles = None

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise TypeError("other_figure must be an instance of class Figure")
        return self.area + other_figure.area


class Square(Figure):
    __angles = 4

    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4


class Circle(Figure):
    __angles = 0

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    @property
    def area(self):
        return pi * self.r ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.r


class Triangle(Figure):
    __angles = 3

    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = self.perimeter / 2.
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    @property
    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Figure):
    __angles = 4

    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2


if __name__ == '__main__':
    s = Square("MySquare", 4)
    c = Circle("MyCircle", 3)
    t = Triangle("MyTriangle", 2, 3, 4)
    r = Rectangle("MyRectangle", 2.1, 3.5)
    figures = [s, c, r, t]
    for f in figures:
        print(f"{f.name:<15s} Area {f.area:<15f} Perimeter {f.perimeter:<15f}")

    print(c.add_area(s))
    print(r.add_area(t))

