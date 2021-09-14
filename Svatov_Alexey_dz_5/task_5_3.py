tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Кондратий', 'Елисей', 'Андрей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tuple_gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses + ([None] * (len(tutors) - len(klasses)))))

print(type(tuple_gen))
print(next(tuple_gen))
print(*tuple_gen)
print(next(tuple_gen))
