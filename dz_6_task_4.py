# *(вместо 3) Решить задачу 3 для ситуации,
# когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить
# объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
#

import json

user_hobbys=[]
user_hobby = {}
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
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

    for user, hobby in user_hobby.items():
        f.write(f'{user.strip()}: {hobby.strip()}\n')


print(user_hobby)



