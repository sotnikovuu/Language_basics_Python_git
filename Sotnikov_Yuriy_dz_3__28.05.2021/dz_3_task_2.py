# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# capitalize

def num_translate_adv(numerator_value):
    vocabulary = {'zero':'ноль',
                  'one':'один',
                  'two':'два',
                  'three':'три',
                  'four':'четыре',
                  'five':'пять',
                  'six':'шесть',
                  'seven':'семь',
                  'eight':'восемь',
                  'nine':'девять',
                  'ten':'десять'}
    if numerator_value[0].isupper() == True:
        numerator_value = numerator_value.lower()
        translation = vocabulary.get(numerator_value, 'none')
        print(translation.capitalize())
    else:
        print(vocabulary.get(numerator_value, 'none'))

num_translate_adv('five')