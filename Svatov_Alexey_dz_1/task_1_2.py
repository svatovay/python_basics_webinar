my_list = []
sum_valid_numbers = 0
sum_valid_numbers_17 = 0
for value in range(1, 1001):
    if value % 2:
        my_list.append(value ** 3)

for number in my_list:
    number_17 = number + 17
    sum_numbers = 0
    sum_numbers_17 = 0
    str_number = str(number)
    str_number_17 = str(number_17)
    idx = 0
    idx_17 = 0
    while idx < len(str_number):
        sum_numbers += int(str_number[idx])
        idx += 1
    if not sum_numbers % 7:
        sum_valid_numbers += number
    while idx_17 < len(str_number_17):
        sum_numbers_17 += int(str_number_17[idx_17])
        idx_17 += 1
    if not sum_numbers_17 % 7:
        sum_valid_numbers_17 += number_17

print(sum_valid_numbers)
print(sum_valid_numbers_17)
