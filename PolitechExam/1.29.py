a = 5
b = 12
c = 13

if (pow(a, 2) + pow(b, 2) - pow(c, 2) == 0) or (pow(b, 2) + pow(c, 2) - pow(a, 2) == 0) or (pow(c, 2) + pow(a, 2) -
                                                                                            pow(b, 2) == 0):
    print("Треугольный прямоугольный")
else:
    print("Треугольник другой")