# Напишите программу, которая определяет наименьшее из четырёх чисел.
#
# Формат входных данных
# На вход программе подаётся четыре целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a < b:
    i = a
else:
    i = b
if c < d:
    j = c
else:
    j = d
if i < j:
    print(i)
else:
    print(j)
