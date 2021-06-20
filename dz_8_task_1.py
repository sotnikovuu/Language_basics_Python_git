# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


mail = {}
RE_EMAIL = re.compile(r'([a-zA-Z0-9._]+)@([.a-zA-Z0-9_]+\.[a-z]+$)')

def email_parse(email_address):
    if RE_EMAIL.findall(email_address):
        email_user_domain = RE_EMAIL.findall(email_address)[0]
        mail = {'username': email_user_domain[0], 'domain': email_user_domain[1]}
        return mail
    else:
        assert RE_EMAIL.findall(email_address), f'ошибка в почтовом адресе {email_address}'

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrains/ru'))
