A: float = float(input("Введите число: "))
N: int = int(input("Введите степень числа: "))

result: list = [item ** N for item in range(1, int(A + 1))]
print(result)