my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_2 = []
for value in my_list:
    if value.isdigit():
        my_list_2.append('"' + value.zfill(2) + '"')
    elif value[1::].isdigit():
        my_list_2.append('"' + value[0] + value[1::].zfill(2) + '"')
    else:
        my_list_2.append(value)
print(my_list_2)
print(' '.join(my_list_2))
