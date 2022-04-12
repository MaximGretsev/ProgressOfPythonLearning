A: int = 10
N: int = int(input("Введите конец последовательности: "))

result = [item for item in range(A, N + 1) if item % 2 != 0 and item % 5 == 0]
print(result)