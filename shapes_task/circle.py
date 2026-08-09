from shape import Shape
from typing import override
import math


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self.__radius = radius

    def get_width(self) -> float:
        return self.__radius * 2

    def get_height(self) -> float:
        return self.__radius * 2

    def get_area(self) -> float:
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    @override
    def __repr__(self) -> str:
        return f"Круг с радиусом {self.__radius!r}"

    @override
    def __eq__(self, other: Circle) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented

        return self.__radius == other.__radius

    @override
    def __hash__(self) -> int:
        return hash(self.__radius)
