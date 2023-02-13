s1, s2, s3, = len(input()), len(input()), len(input())
max_len = max(s1, s2, s3)
min_len = min(s1, s2, s3)
everage = (s1 + s2 + s3) - (max_len + min_len)
if max_len - everage == everage - min_len:
    print('YES')
else:
    print('NO')