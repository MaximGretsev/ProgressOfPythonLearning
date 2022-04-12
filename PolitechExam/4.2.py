A: int = 5
B: int = 29
result: list = [item for item in range(A - 1, B)[::-1]]
# print([i for i in result[::-1]])
print(result)
print(f'Количество элементов в списке: {len(result)}')