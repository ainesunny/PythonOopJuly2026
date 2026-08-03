from shapes import Shape, Square, Rectangle, Triangle, Circle


def get_max_area_shape(shapes_list: list[Shape]) -> Shape:
    area_sorted_shapes = sorted(shapes_list, key=lambda shape: shape.get_area())
    return area_sorted_shapes[-1]


def get_second_perimeter_shape(shapes_list: list[Shape]) -> Shape:
    perimeter_sorted_shapes = sorted(shapes_list, key=lambda shape: shape.get_perimeter())
    return perimeter_sorted_shapes[-2]


square_1 = Square(5.0)
square_2 = Square(7.5)

rectangle_1 = Rectangle(34.5, 6.0)
rectangle_2 = Rectangle(10.0, 2.1)

triangle_1 = Triangle(1.5, 2.3, 7.8, 11.1, 3.2, 6.7)
triangle_2 = Triangle(0.5, 0.5, 9.2, 3.8, 2.1, 8.4)

circle_1 = Circle(13.7)
circle_2 = Circle(7.2)

shapes = [square_1, square_2, rectangle_1, rectangle_2, triangle_1, triangle_2, circle_1, circle_2]
print(f"Список фигур: {shapes}")

max_area_shape = get_max_area_shape(shapes)
print(f"Фигура с самой большой площадью: {max_area_shape}")

second_perimeter_shape = get_second_perimeter_shape(shapes)
print(f"Фигура со вторым по величине периметром: {second_perimeter_shape}")
