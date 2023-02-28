string = input().lower()
count_gl = 0
count_sog = 0
gl = 'ауоыиэяюёе'
sog = 'бвгджзйклмнпрстфхцчшщ'
for i in string:
    if i in gl:
        count_gl += 1
    if i in sog:
        count_sog += 1
print(f'Количество гласных букв равно {count_gl}')
print(f'Количество согласных букв равно {count_sog}')