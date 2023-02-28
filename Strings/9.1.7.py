string = input()
counter_plus = 0
counter_star = 0
for i in string:
    if '+' in i:
        counter_plus += 1
    if '*' in i:
        counter_star += 1
print(f'Символ + встречается {counter_plus} раз')
print(f'Символ + встречается {counter_star} раз')