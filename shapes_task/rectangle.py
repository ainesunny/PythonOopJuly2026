from shape import Shape
from typing import override


class Rectangle(Shape):
    def __init__(self, first_rectangle_side: float, second_rectangle_side: float) -> None:
        self.__first_rectangle_side = first_rectangle_side
        self.__second_rectangle_side = second_rectangle_side

    @property
    def first_rectangle_side(self) -> float:
        return self.__first_rectangle_side

    @first_rectangle_side.setter
    def first_rectangle_side(self, first_rectangle_side: float) -> None:
        self.__first_rectangle_side = first_rectangle_side

    @property
    def second_rectangle_side(self) -> float:
        return self.__second_rectangle_side

    @second_rectangle_side.setter
    def second_rectangle_side(self, second_rectangle_side: float) -> None:
        self.__second_rectangle_side = second_rectangle_side

    def get_width(self) -> float:
        return self.__first_rectangle_side

    def get_height(self) -> float:
        return self.__second_rectangle_side

    def get_area(self) -> float:
        return self.__first_rectangle_side * self.__second_rectangle_side

    def get_perimeter(self) -> float:
        return (self.__first_rectangle_side + self.__second_rectangle_side) * 2

    @override
    def __repr__(self) -> str:
        return f"Прямоугольник со сторонами {self.__first_rectangle_side!r} и {self.__second_rectangle_side!r}"

    @override
    def __eq__(self, other: Rectangle) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return (self.__first_rectangle_side == other.__first_rectangle_side
                and self.__second_rectangle_side == other.__second_rectangle_side)

    @override
    def __hash__(self) -> int:
        return hash((self.__first_rectangle_side, self.__second_rectangle_side))
