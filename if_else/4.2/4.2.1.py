# Напишите программу, которая принимает целое число
# �
# x и определяет, принадлежит ли данное число указанному промежутку.
#
# Формат входных данных
# На вход программе подаётся целое число
# �
# x.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')