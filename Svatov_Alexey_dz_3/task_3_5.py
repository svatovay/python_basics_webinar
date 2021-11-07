from random import shuffle


def get_jokes(n):
    """Create n-jokes from 3 lists and return list of jokes"""
    list_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    for noun, adverb, adjective in zip(nouns[:n], adverbs[:n], adjectives[:n]):
        list_jokes.append(' '.join([noun, adverb, adjective]))
    return list_jokes


print(get_jokes(int(input('Введите количество шуток (не более 5): '))))
