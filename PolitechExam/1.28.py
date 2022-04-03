sale = 0.01
summa = int(input("Введите стоимость покупки: "))
if summa > 1000:
    print(f"Цена с учетом скидки: {round(summa / (1 + sale), 1)}")
