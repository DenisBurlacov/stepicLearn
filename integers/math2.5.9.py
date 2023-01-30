num = int(input())
last_num = num % 10
third_num = (num % 100) // 10
second_num = (num % 1000) // 100
first_num = num // 1000
print(f'Цифра в позиции тысяч равна {first_num}')
print(f'Цифра в позиции сотен равна {second_num}')
print(f'Цифра в позиции десятков равна {third_num}')
print(f'Цифра в позиции единиц равна {last_num}')

