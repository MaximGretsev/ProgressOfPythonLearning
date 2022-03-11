int_a, int_b, int_c = input('Enter number: ').split(' ')
int_a = int(int_a)
int_b = int(int_b)
int_c = int(int_c)
if int_a < 45 or int_b < 45 or int_c < 45:
    print('Одно из чисел меньше 45')
elif int_a == 45 or int_b == 45 or int_c == 45:
    print('Одно из чисел равно 45')
else:
    print('Все числа больше 45')