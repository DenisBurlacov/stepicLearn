num = int(input())
last_num = num % 10
midl_num = (num % 100) // 10
first_num = num // 100
print(num)
print(first_num, last_num, midl_num, sep='')
print(midl_num, first_num, last_num, sep='')
print(midl_num, last_num, first_num,  sep='')
print(last_num, first_num, midl_num, sep='')
print(last_num, midl_num, first_num, sep='')


