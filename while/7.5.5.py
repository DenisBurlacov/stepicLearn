num = int(input())
while num > 9:
    second = num % 10
    num = num // 10
print(second)