# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов
# в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать
# аргументы именованными?

from random import randrange


def get_jokes(quantity, repetitions=True):
    """
    Функция возвращает сгенерированные шутки

    quantity - кол-во сгенерированных шуток

    repetitions - разрешить (True) / запретить (False) повторять слова
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    num = 0
    while num < quantity:
        joke = []
        choice_nouns = nouns[randrange(len(nouns))]
        joke.append(choice_nouns)

        choice_adverbs = adverbs[randrange(len(adverbs))]
        joke.append(choice_adverbs)

        choice_adjectives = adjectives[randrange(len(adjectives))]
        joke.append(choice_adjectives)

        if not repetitions:
            nouns.remove(choice_nouns)
            adverbs.remove(choice_adverbs)
            adjectives.remove(choice_adjectives)

        jokes.append(' '.join(joke))
        num += 1
    print(jokes)


get_jokes(2, False)