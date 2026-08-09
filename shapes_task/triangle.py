from shape import Shape
from typing import override
import math


class Triangle(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float) -> None:
        self.__x1 = x1

    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float) -> None:
        self.__y1 = y1

    @property
    def x2(self) -> float:
        return self.__x2

    @x2.setter
    def x2(self, x2: float) -> None:
        self.__x2 = x2

    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float) -> None:
        self.__y2 = y2

    @property
    def x3(self) -> float:
        return self.__x3

    @x3.setter
    def x3(self, x3: float) -> None:
        self.__x3 = x3

    @property
    def y3(self) -> float:
        return self.__y3

    @y3.setter
    def y3(self, y3: float) -> None:
        self.__y3 = y3

    def get_width(self) -> float:
        return max(self.__x1, self.__x2, self.__x3) - min(self.__x1, self.__x2, self.__x3)

    def get_height(self) -> float:
        return max(self.__y1, self.__y2, self.__y3) - min(self.__y1, self.__y2, self.__y3)

    def get_area(self) -> float:
        return abs(
            ((self.__x2 - self.__x1) * (self.__y3 - self.__y1) - (self.__x3 - self.__x1) * (self.__y2 - self.__y1))) / 2

    @staticmethod
    def get_side_length(x_first: float, y_first: float, x_second: float, y_second: float) -> float:
        return math.sqrt((x_second - x_first) ** 2 + (y_second - y_first) ** 2)

    def get_perimeter(self) -> float:
        first_triangle_side_length = self.get_side_length(self.__x1, self.__y1, self.__x2, self.__y2)
        second_triangle_side_length = self.get_side_length(self.__x2, self.__y2, self.__x3, self.__y3)
        third_triangle_side_length = self.get_side_length(self.__x3, self.__y3, self.__x1, self.__y1)
        return first_triangle_side_length + second_triangle_side_length + third_triangle_side_length

    @override
    def __repr__(self) -> str:
        return (f"Треугольник с координатами вершин ({self.__x1!r}, {self.__y1!r}); ({self.__x2!r}, {self.__y2!r}); "
                f"({self.__x3!r}, {self.__y3!r})")

    @override
    def __eq__(self, other: Triangle) -> bool:
        if not isinstance(other, Triangle):
            return NotImplemented

        return (self.__x1 == other.__x1 and self.__x2 == other.__x2 and self.__x3 == other.__x3
                and self.__y1 == other.__y1 and self.__y2 == other.__y2 and self.__y3 == other.__y3)

    @override
    def __hash__(self) -> int:
        return hash((self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3))
