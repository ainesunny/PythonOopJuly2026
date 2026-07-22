from range import Range

user_range_1 = Range(int(input("Введите начало первого диапазона: ")), int(input("Введите конец первого диапазона: ")))

print(f"Вы ввели первый диапазон {str(user_range_1)} длиной {user_range_1.get_length()}")

user_range_2 = Range(int(input("Введите начало второго диапазона: ")), int(input("Введите конец второго диапазона: ")))

print(f"Вы ввели второй диапазон {str(user_range_2)} длиной {user_range_2.get_length()}")

user_number = int(input("Введите число: "))

if user_range_1.is_inside(user_number) and user_range_2.is_inside(user_number):
    print(f"Введенное число {user_number} входит в оба диапазона")
elif user_range_1.is_inside(user_number):
    print(f"Введенное число {user_number} входит только в первый диапазон {str(user_range_1)}")
elif user_range_2.is_inside(user_number):
    print(f"Введенное число {user_number} входит только во второй диапазон {str(user_range_2)}")
else:
    print(f"Введенное число {user_number} не входит ни в один из двух диапазонов")

intersection_range = user_range_1.intersection(user_range_2)

if intersection_range is not None:
    print(f"Интервал пересечения двух указанных диапазонов {str(intersection_range)}")
else:
    print("У указанных диапазонов нет пересечения")

union_range = user_range_1.union(user_range_2)

print(f"Объединенный интервал из двух указанных диапазонов {[str(element) for element in union_range]}")

difference_range = user_range_1.difference(user_range_2)

if isinstance(difference_range, int):
    print(f"Разность диапазонов (из первого вычитается второй) {difference_range}")
else:
    print(f"Разность диапазонов (из первого вычитается второй) {[str(element) for element in difference_range]}")
