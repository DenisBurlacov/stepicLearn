counter = 0
n = int(input())
for i in range(n):
    if i % 2 == 0:
        counter += i + 1
    else:
        counter -= i + 1
print(counter)