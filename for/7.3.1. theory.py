# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter += 1
# print('You entered', counter, 'number the bigger than 10')

# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 += 1
#     if num == 0:
#         counter2 += 1
# print('Yo entered', counter1, 'numbers that bigger than ten')
# print('Yo entered', counter2, 'numbers that equal to 0')

# total = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         total += num
# print('Summ of numbers that bigger of ten equal', total)

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % 2 == 0:
#         flag = False
# if num == 1:
#     print('this is the one')
# elif flag == True:
#     print('simple num')
# else:
#     print('the num is difulct')
largest = -1
for i in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('the largest num is,', largest)