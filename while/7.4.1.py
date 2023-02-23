# s = input()
# count = 0
# while s != 'стоп' and s != 'хватит' and s != 'достаточно':
#     count += 1
#     s = input()
# print(count)

a = 0
while input() not in ("стоп", "хватит", "достаточно"):
    a += 1
print(a)