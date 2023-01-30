num = int(input())
last_num = num % 10
midl_num = (num % 100) // 10
first_num = num // 100
summ = last_num + midl_num + first_num
multipl = last_num * midl_num * first_num
print(f'Сумма цифр = {summ}')
print(f'Произведение цифр = {multipl}')