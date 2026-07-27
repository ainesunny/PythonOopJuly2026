from range import Range

user_range_1_start = float(input("Введите начало первого диапазона: "))
user_range_1_end = float(input("Введите конец первого диапазона: "))
user_range_1 = Range(user_range_1_start, user_range_1_end)

print(f"Вы ввели первый диапазон {user_range_1} длиной {user_range_1.length}")

user_range_2_start = float(input("Введите начало второго диапазона: "))
user_range_2_end = float(input("Введите конец второго диапазона: "))
user_range_2 = Range(user_range_2_start, user_range_2_end)

print(f"Вы ввели второй диапазон {user_range_2} длиной {user_range_2.length}")

user_number = int(input("Введите число: "))

if user_range_1.is_inside(user_number) and user_range_2.is_inside(user_number):
    print(f"Введенное число {user_number} входит в оба диапазона")
elif user_range_1.is_inside(user_number):
    print(f"Введенное число {user_number} входит только в первый диапазон {user_range_1}")
elif user_range_2.is_inside(user_number):
    print(f"Введенное число {user_number} входит только во второй диапазон {user_range_2}")
else:
    print(f"Введенное число {user_number} не входит ни в один из двух диапазонов")

intersection = user_range_1.get_intersection(user_range_2)

if intersection is not None:
    print(f"Интервал пересечения двух указанных диапазонов {intersection}")
else:
    print("У указанных диапазонов нет пересечения")

union = user_range_1.get_union(user_range_2)

print(f"Объединенный интервал из двух указанных диапазонов {[element for element in union]}")

difference = user_range_1.get_difference(user_range_2)

if len(difference) == 0:
    print(f"Разность диапазонов (из первого вычитается второй) = 0")
else:
    print(f"Разность диапазонов (из первого вычитается второй) {[element for element in difference]}")
