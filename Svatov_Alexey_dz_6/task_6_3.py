from itertools import zip_longest

users = open('users.csv', 'r', encoding='utf-8')
hobby = open('hobby.csv', 'r', encoding='utf-8')
with open('dict_users.txt', 'w', encoding='utf=8') as dict_file:
    dict_users = {(user.strip() if user else user): (hobby_1.strip() if hobby_1 else hobby_1) for user, hobby_1 in
                  zip_longest(users, hobby)}
    if None in dict_users:
        dict_file.write('1')
    else:
        dict_file.write(f'{dict_users}')

users.close()
hobby.close()
