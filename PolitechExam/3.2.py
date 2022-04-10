mast: int = int(input("Выберете число от 1 до 4: "))
values: int = int(input("Выберете желаемую карту от 6 до 14: "))
dict_mast: dict = {1: "Пики", 2: "Трефы", 3: "Бубны", 4: "Червы"}
dict_value: dict = {6: "Шестёрка", 7: "Семёрка", 8: "Восьмёрка", 9: "Девятка", 10: "Десятка", 11: "Валет", 12: "Дама",
              13: "Король", 14: "Туз"}
if mast not in dict_mast:
    raise ValueError("Ваше число вне диапазона")
else:
    print(dict_mast[mast], end=" ")
if values not in dict_value:
    raise ValueError("Вы ввели не верное значение :(")
else:
    print(dict_value[values])
    