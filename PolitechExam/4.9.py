import random

sequence: list = [random.randint(1, 20)for _ in range(20)]
arr: list = [item ** 2 if item % 2 == 0 else item + item for item in sequence]
print(sequence, len(sequence))
print(arr, len(arr))