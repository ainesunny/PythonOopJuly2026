from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self) -> float:
        pass

    @abstractmethod
    def get_height(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side_length: float) -> None:
        self.__side_length = side_length

    @property
    def side_length(self) -> float:
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length: float) -> None:
        self.__side_length = side_length

    def get_width(self) -> float:
        return self.__side_length

    def get_height(self) -> float:
        return self.__side_length

    def get_area(self) -> float:
        return self.__side_length ** 2

    def get_perimeter(self) -> float:
        return self.__side_length * 4

    def __repr__(self) -> str:
        return f"Квадрат со стороной {self.__side_length!r}"


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

    def get_perimeter(self) -> float:
        side_a = math.sqrt((self.__x2 - self.__x1) ** 2 + (self.__y2 - self.__y1) ** 2)
        side_b = math.sqrt((self.__x3 - self.__x2) ** 2 + (self.__y3 - self.__y2) ** 2)
        side_c = math.sqrt((self.__x1 - self.__x3) ** 2 + (self.__y1 - self.__y3) ** 2)
        return side_a + side_b + side_c

    def __repr__(self) -> str:
        return (f"Треугольник с координатами вершин ({self.__x1!r}, {self.__y1!r}); ({self.__x2!r}, {self.__y2!r}); "
                f"({self.__x3!r}, {self.__y3!r})")


class Rectangle(Shape):
    def __init__(self, side_a: float, side_b: float) -> None:
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self) -> float:
        return self.__side_a

    @side_a.setter
    def side_a(self, side_a: float) -> None:
        self.__side_a = side_a

    @property
    def side_b(self) -> float:
        return self.__side_b

    @side_b.setter
    def side_b(self, side_b: float) -> None:
        self.__side_b = side_b

    def get_width(self) -> float:
        return self.__side_a

    def get_height(self) -> float:
        return self.__side_b

    def get_area(self) -> float:
        return self.__side_a * self.__side_b

    def get_perimeter(self) -> float:
        return (self.__side_a + self.__side_b) * 2

    def __repr__(self) -> str:
        return f"Прямоугольник со сторонами {self.__side_a!r} и {self.__side_b!r}"


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
        return math.pi * self.__radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __repr__(self) -> str:
        return f"Круг с радиусом {self.__radius!r}"
