import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def square(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def square(self):
        return self._a * self._b


class Circle(Shape):
    def __init__(self, r):
        self._r = r

    def square(self):
        return math.pi * self._r ** 2


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

class Triangle(Shape):
    def __init__(self, b, h):
        self._h, self._b = h, b

    def square(self):
        return self._b * self._h * 0.5


if __name__ == "__main__":
    shapes = [Triangle(10, 5), Square(2), Circle(3), Rectangle(5, 3)]
    for s in shapes:
        print(s.square())