from shape import Shape
from typing import override


class Square(Shape):
    def __init__(self, side_length: float) -> None:
        self.__side_length = side_length

    @property
    def side_length(self) -> float:
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length: float) -> None:
        self.__side_length = side_length

    @override
    def get_width(self) -> float:
        return self.__side_length

    @override
    def get_height(self) -> float:
        return self.__side_length

    @override
    def get_area(self) -> float:
        return self.__side_length * self.__side_length

    @override
    def get_perimeter(self) -> float:
        return self.__side_length * 4

    @override
    def __repr__(self) -> str:
        return f"Квадрат со стороной {self.__side_length!r}"

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Square):
            return NotImplemented

        return self.__side_length == other.__side_length

    @override
    def __hash__(self) -> int:
        return hash(self.__side_length)
