n = int(input())
last_num = n % 10
while n != 0:
    num = n % 10
    if num == last_num:
        result = 'YES'
    else:
        result = 'NO'
        break
    n = n // 10
print(result)