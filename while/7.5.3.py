n = int(input())
max_num = 0
min_num = 9

while n != 0:
    if n % 10 > max_num:
        max_num = n % 10
    if n % 10 < min_num:
        min_num = n % 10
    n = n // 10
print(f'Максимальная цифра равна {max_num}')
print(f'Минимальная цифра равна {min_num}')