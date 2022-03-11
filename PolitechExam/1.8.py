int_a = int(input('Enter number: '))

if (int_a % 2 == 0 and int_a % 7 == 0) and (int_a // 11 != 0 and int_a // 13 != 0):
    print('True')
else:
    print('False')