int_a = int(input('Enter number: '))

if (int_a % 3 != 0 and (int_a % 7 == 0 and int_a % 10 == 0)):
    print('True')
else:
    print('False')