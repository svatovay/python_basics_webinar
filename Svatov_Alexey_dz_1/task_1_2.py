my_list = []
sum_valid_numbers = 0
sum_valid_numbers_mod = 0
MOD = 17
for value in range(1, 1001):
    if value % 2:
        my_list.append(value ** 3)
for number in my_list:
    number_mod = number + MOD
    sum_numbers = 0
    sum_numbers_mod = 0
    digit = 1
    digit_mod = 1
    digit_number = 0
    digit_number_mod = 0
    number_copy = number
    number_copy_mod = number_mod
    while number_copy:
        digit *= 10
        digit_number = number_copy % digit
        sum_numbers += digit_number // (digit // 10)
        number_copy -= digit_number
    if not sum_numbers % 7:
        sum_valid_numbers += number
    while number_copy_mod:
        digit_mod *= 10
        digit_number_mod = number_copy_mod % digit_mod
        sum_numbers_mod += digit_number_mod // (digit_mod // 10)
        number_copy_mod -= digit_number_mod
    if not sum_numbers_mod % 7:
        sum_valid_numbers_mod += number_mod
print(sum_valid_numbers)
print(sum_valid_numbers_mod)
