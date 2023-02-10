num = int(input())
if num == 0:
    print('зеленый')
elif (1 <= num <= 10 or 19 <= num <= 28) and num % 2 == 0:
    print('черный')
elif (1 <= num <= 10 or 19 <= num <= 28) and num % 2 != 0:
    print('красный')
elif (11 <= num <= 18 or 29 <= num <= 36) and num % 2 == 0:
    print('красный')
elif (11 <= num <= 18 or 29 <= num <= 36) and num % 2 != 0:
    print('черный')
else:
    print('ошибка ввода')
