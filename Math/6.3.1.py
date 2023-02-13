from math import pow, sqrt
a, b, c, d = float(input()), float(input()), float(input()), float(input())
num = sqrt(pow(a - c, 2) + pow(b - d, 2))
print(num)
