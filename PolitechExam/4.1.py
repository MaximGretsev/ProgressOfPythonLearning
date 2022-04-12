A: int = 5
B: int = 29

result: list = [item for item in range(A, B + 1)]
print(result)
print(f'Количество чисел в последовательности: {len(result)}')