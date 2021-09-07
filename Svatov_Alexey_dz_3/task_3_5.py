from random import shuffle


def get_jokes(n):
    list_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
        list_jokes.append(' '.join([noun, adverb, adjective]))
    return list_jokes[:n]


print(get_jokes(int(input('Введите количество шуток (не более 5): '))))

#сделать документирование и именнованные аргументы
