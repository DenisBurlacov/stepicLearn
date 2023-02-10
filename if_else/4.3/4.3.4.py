months_num = int(input())
non_leap_month = 28
month_thirty_days = 30
month_thirty_one_day = 31
if months_num == 2:
    print(non_leap_month)
elif months_num == 4 or months_num == 6 or months_num == 9 or months_num == 11:
    print(month_thirty_days)
else:
    print(month_thirty_one_day)

# Second variant for solving task---------------------------------------------------------------

# x = int(input())
# if x == 2:
#     print(28)
# elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
#     print(30)
# else:
#     print(31)