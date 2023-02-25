# i = 0
# while i < 10:
#     print('Hello')
#     i += 1

# num = int(input())
# while num != -1:
#     print('the squeare of your number equel:', num * num)
#     num = int(input())

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('the summ of the numbers equel', total)
# # num = int(input())
# has_sever = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_sever = True
#     num = num // 10
#
# if has_sever:
#     print('YES')
# else:
#     print('NO')
# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# for seconds in range(1, 60 + 1):
#     print(seconds)

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')