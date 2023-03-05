string_quantity = int(input())
counter = 0
for i in range(string_quantity):
    s = input()
    if s.count('11') > 2:
        counter += 1
print(counter)
