a = int(input("Введите первое число (a): "))  # Получаем первое число
b = int(input("Введите второе число (b): "))  # Получаем второе число
if a == b:  # Сравниваем равны ли два числа
    print(f"Число {a} и число {b} равны")
else:
    min_number = a if a < b else b  # Проверяем, что из них больше
    print(f"Наименьшее число из {a} и {b} - число {min_number}")  # Выводим результат
