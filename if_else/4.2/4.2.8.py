x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = x2 - x1
b = y2 - y1
if -1 <= a <= 1 and -1 <= b <= 1:
    print('YES')
else:
    print('NO')