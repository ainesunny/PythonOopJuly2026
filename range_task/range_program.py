from range import Range

user_range = Range(int(input("Введите начало диапазона: ")), int(input("Введите конец диапазона: ")))

print(f"Вы ввели диапазон [{user_range.start}; {user_range.end}] длиной {user_range.get_length()}")

user_number = float(input("Введите число: "))

if user_range.is_inside(user_number):
    print(f"Введенное число {user_number} входит в диапазон [{user_range.start}; {user_range.end}]")
else:
    print(f"Введенное число {user_number} не входит в диапазон [{user_range.start}; {user_range.end}]")
