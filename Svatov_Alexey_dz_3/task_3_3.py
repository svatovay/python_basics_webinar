def thesaurus(*args):
    dict_names = {}
    for name in args:
        if dict_names.get(name[0]):
            dict_names[name[0]].append(name)
        else:
            dict_names.setdefault(name[0], [name])
    return dict_names


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
