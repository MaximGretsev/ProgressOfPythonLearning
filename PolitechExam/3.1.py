percent_1 = 0.2 
percent_2 = 0.22
deposit: int = int(input("Сколько вы хотите положить денег? "))
if deposit < 5000:
    print(f'Вы заработаете {deposit * percent_1}')
elif 5000 < deposit < 10000:
    print(f'Вы заработаете {deposit * percent_2}')
else:
    print(f'У вас очень много деняк')