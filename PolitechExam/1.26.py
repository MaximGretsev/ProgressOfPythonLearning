percent_half_year = 6
percent_year = 8
per_month = (percent_half_year / 12) / 100
per_month_year = (percent_year / 12) / 100

deposit = int(input("Введите, сколько хотите положить денег: "))
period = int(input("Введите, на сколько месяцев вы хотите положить деньги: "))
if 6 <= period <= 12:
    result = per_month * deposit
    print(f"В месяц вы будете получать: {result}")
    print(f"Всего вы заработаете за {period} месяцев сумму {result * period}")
elif period >= 12:
    result = per_month_year * deposit
    print(f"В месяц вы будете получaть: {result}")
    print(f"Всего за {period} месяцев вы получите {result * period}")