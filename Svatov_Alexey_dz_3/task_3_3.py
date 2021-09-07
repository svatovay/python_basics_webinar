def thesaurus(name_tuple):
    dict_names = {}
    for name in name_tuple:
        if dict_names.get(name[0]):
            dict_names[name[0]].append(name)
        else:
            dict_names.setdefault(name[0], [name])
    return dict_names


print(thesaurus(tuple(input('Введите имена через запятую: ').split(', '))))
