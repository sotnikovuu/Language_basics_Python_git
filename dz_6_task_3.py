# Есть два файла: в одном хранятся ФИО пользователей сайта,
# a 3
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи


from itertools import zip_longest
import json


user_hobby = {}
with open('users.csv', encoding='utf-8') as f_users:
    with open('hobby.csv', encoding='utf-8') as f_hobby:
        line_users = sum(1 for line in f_users)
        line_hobby = sum(1 for line in f_hobby)

        if line_users < line_hobby:
            exit(1)

        f_users.seek(0)
        f_hobby.seek(0)

        for user in f_users:
            user_hobby.setdefault(user.strip().replace(',',' '), f_hobby.readline().strip() or 'None')

with open('user_hobby.json', 'w', encoding='utf-8') as f_user_hobby:
    json.dump(user_hobby, f_user_hobby, ensure_ascii=False)

print(user_hobby)







