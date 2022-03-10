int_a = int(input('Введи число A: '))

# if len(int_a) == 3:
#     print('Число трехзначное')
# else:
#     print('Число не трехзначное')

if int_a >= 100 and int_a <= 999:
    print('Трехзначное')
else:
    print('Не Трехзначное')