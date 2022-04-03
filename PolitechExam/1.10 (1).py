A = 3
B = 3
C = 3
D = 6

print((A % 2 == 0 and B % 2 == 0) or \
      (A % 2 == 0 and C % 2 == 0) or \
      (A % 2 == 0 and D % 2 == 0) or \
      (B % 2 == 0 and D % 2 == 0) or \
      (C % 2 == 0 and C % 2 == 0))