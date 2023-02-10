distance = float(input())
spead_one = float(input())
spead_two = float(input())
spead_both = spead_one + spead_two
time = distance / spead_both
print(time)

year = int(input())
if year > 2:
    print(21 + (year - 2) * 4)
elif year <= 2:
    print(year * 10.5)
