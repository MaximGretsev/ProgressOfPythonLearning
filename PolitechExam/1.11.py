int_a, int_b = input('Введите числа через пробел: ').split(' ')
int_a = int(int_a)
int_b = int(int_b)

if (int_a % 2 == 0 and int_b % 2 != 0) or (int_b % 2 == 0 and int_a % 2 != 0):
    print('Одно из чисел четное')
else:
    print('Или оба числа четные, или оба числа не четные')