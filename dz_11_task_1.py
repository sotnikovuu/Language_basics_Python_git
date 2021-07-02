# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self.MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self.MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        # [' ', ' ', ' ', ' ', 10, 5, 9, 7, 6]


        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self.MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)


    def output(self):
        # Форматированный вывод карточки с названием.
        player_type = ' ' + self.player_type + ' '
        if len(player_type) <= 24:
            print(player_type.center(26, '-'))
        else:
            print('-' * 26)
        for y in self._matrix:
            string = ''
            for x in y:
                if not x:
                    string += '   '
                elif x == -1:
                    string += ' - '
                else:
                    string += '{:>2} '.format(str(x))
            print(string)
        print('-' * 26)

        # def barrel_generation(self):
        #     variation = list(range(1, self._MAX_NUMBER + 1))
        #     barrel = random.choice(variation)
        #     variation.remove(barrel)
        #     return barrel


class Players:
    human = LotoCard
    computer = LotoCard


class LotoGame:
    variation = list(range(1, 90))
    barrel = random.choice(variation)
    variation.remove(barrel)

    # def barrel_generation(variation):
    #     # variation = list(range(1, LotoCard))
    #     barrel = random.choice(variation)
    #     variation.remove(barrel)
    #     return barrel
    a = Players



a = LotoCard
print(a.output())
a.output


# LotoGame
