import random
sequence: list = [random.randint(1, 20) for _ in range(10)]
a = 2
b = 3
list_ = []
for i in range(len(sequence)):
    if sequence[i] % 2 == 0:
        list_.append(sequence[i] + a)
    elif i % 2 == 0:
        list_.append(sequence[i] - b)
    else:
        list_.append(i)
print(sequence)
print(list_)

# Кажется, это полнейшая борода, что я тут понаписал. Но какаво было задание ¯\_(ツ)_/¯