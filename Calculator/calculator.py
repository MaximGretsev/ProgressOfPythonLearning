a = float(input('Введи число а: '))
b = float(input('Введи число b: '))
c = input('Введи операцию: ')

match c:
    case '/' if b != 0:
        print(a / b)
    case '%' if b != 0:
        print(a % b)
    case '//' if b != 0:
        print(a // b)
    case '**':
        print(a ** b)
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case _:
        print('Деление на ноль!')
