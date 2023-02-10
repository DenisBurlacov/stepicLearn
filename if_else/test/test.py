# s = int(input())
# b = s % 10
# g = s % 100 // 10
# if b == 0 and g == 0:
#     print('YES')
# else:
#     print('NO')

year = int(input())
gender = input()
if gender == 'f' and 10 <= year <= 15:
    print('YES')
else:
    print('NO')