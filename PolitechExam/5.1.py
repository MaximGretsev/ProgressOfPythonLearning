n: int = 5
while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = ((n * 3) + 1) // 2 
    print(n)
    