import random

sequence: list = [random.randint(1, 20) * _ for _ in range(20)]
print(sequence, len(sequence))