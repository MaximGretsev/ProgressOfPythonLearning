sequence: list = [-1, 0, 5, -6, 7, -8, 10, 2, -3]

result: list = [item for item in sequence if item < 0]
odd: list = [i for i in range(len(sequence)) if i % 2 != 0]
count: int = 1
for item in result:
    count *= item

print(len(result))
print(count)
print(sum(odd))