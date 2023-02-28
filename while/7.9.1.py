n = int(input())
counter = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(counter, end='')
        counter += 1
    print()

# for row in range(1, 30):
#     for i in range(30 - row):
#         print(' ', end=' ')
#     for i in range(1, row):
#         if i < 10:
#             print(i, end=' ')
#         else:
#             print(i, end='')
#     for i in range(row, 0, -1):
#         if i < 10:
#             print(i, end=' ')
#         else:
#             print(i, end='')
#     print()
# for j in range(30):
#     for i in range(j + 2):
#         print(' ', end=' ')
#     for i in range(1, 29 - j):
#         if i < 10:
#             print(i, end=' ')
#         else:
#             print(i, end='')
#     for i in range(27 - j, 0, -1):
#         if i < 10:
#             print(i, end=' ')
#         else:
#             print(i, end='')
#     print()