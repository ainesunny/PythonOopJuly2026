from range import Range

range_1_start = float(input("Введите начало первого диапазона: "))
range_1_end = float(input("Введите конец первого диапазона: "))
range_1 = Range(range_1_start, range_1_end)

print(f"Вы ввели первый диапазон {range_1} длиной {range_1.length}")

range_2_start = float(input("Введите начало второго диапазона: "))
range_2_end = float(input("Введите конец второго диапазона: "))
range_2 = Range(range_2_start, range_2_end)

print(f"Вы ввели второй диапазон {range_2} длиной {range_2.length}")

number = float(input("Введите число: "))

if range_1.is_inside(number) and range_2.is_inside(number):
    print(f"Введенное число {number} входит в оба диапазона")
elif range_1.is_inside(number):
    print(f"Введенное число {number} входит только в первый диапазон {range_1}")
elif range_2.is_inside(number):
    print(f"Введенное число {number} входит только во второй диапазон {range_2}")
else:
    print(f"Введенное число {number} не входит ни в один из двух диапазонов")

intersection = range_1.get_intersection(range_2)

if intersection is not None:
    print(f"Интервал пересечения двух указанных диапазонов {intersection}")
else:
    print("У указанных диапазонов нет пересечения")

union = range_1.get_union(range_2)

print(f"Объединенный интервал из двух указанных диапазонов {[element for element in union]}")

difference = range_1.get_difference(range_2)

if len(difference) == 0:
    print("Разность диапазонов (из первого вычитается второй) = 0")
else:
    print(f"Разность диапазонов (из первого вычитается второй) {[element for element in difference]}")
