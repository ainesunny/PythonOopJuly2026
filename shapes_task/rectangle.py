from shape import Shape
from typing import override


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float) -> None:
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float) -> None:
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_area(self) -> float:
        return self.__width * self.__height

    def get_perimeter(self) -> float:
        return (self.__width + self.__height) * 2

    @override
    def __repr__(self) -> str:
        return f"Прямоугольник со сторонами {self.__width!r} и {self.__height!r}"

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return (self.__width == other.__width
                and self.__height == other.__height)

    @override
    def __hash__(self) -> int:
        return hash((self.__width, self.__height))
