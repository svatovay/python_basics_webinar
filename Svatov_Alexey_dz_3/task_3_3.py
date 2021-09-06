name_tuple = ('Мария', 'Пётр', 'Марк', 'Серж', 'Сергей')
dict_names = {}
for name in name_tuple:
    if dict_names.get(name[0]):
        dict_names[name[0]] = list(map(str, name_tuple))
    else:
        dict_names.setdefault(name[0], list(map(str, name_tuple)))
print(dict_names)
# Доделать!!! значения к ключам должны делать списком (даже, если одно значение)
