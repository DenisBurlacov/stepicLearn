first_sity = input()
second_sity = input()
third_sity = input()
len_first = len(first_sity)
len_second = len(second_sity)
len_third = len(third_sity)
if len_first > len_second > len_third:
    max_len = first_sity
    min_len = third_sity
elif len_first > len_third > len_second:
    max_len = first_sity
    min_len = second_sity
elif len_second > len_first > len_third:
    max_len = second_sity
    min_len = third_sity
elif len_second > len_third > len_first:
    max_len = second_sity
    min_len = first_sity
elif len_third > len_first > len_second:
    max_len = third_sity
    min_len = second_sity
else:
    max_len = third_sity
    min_len = first_sity
print(min_len)
print(max_len)