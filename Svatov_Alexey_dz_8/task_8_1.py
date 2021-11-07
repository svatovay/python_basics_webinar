import re

RE_EMAIL = re.compile(r'([A-Z]|[a-z]|\d|\.)+@([A-Z]|[a-z]|\d)+\.[a-z]+')


def email_parse(email):
    if RE_EMAIL.match(email):
        email_dict = {'username': email.split('@')[0], 'domain': email.split('@')[1]}
    else:
        raise ValueError(f'wrong email: {email}')
    return email_dict


print(email_parse('someone@geekbrains.ru'))
