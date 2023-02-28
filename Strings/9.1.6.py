s = input()
result = ''
for i in s:
    if i in '0123456789':
        result = 'Цифра'
        break
    else:
        result = 'Цифр нет'

print(result)