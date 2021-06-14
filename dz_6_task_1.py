# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

from requests import get, utils


response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
file_logs = (response.content.decode(encoding=encodings))

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(file_logs)
    f.close()

f = open('nginx_logs.txt')
strings = f.readlines()
list_tuples = []
num = 0
while num <= len(strings) - 1:
    remote_addr = strings[num][:strings[num].find('-')]
    request_type = strings[num][strings[num].find('G'):strings[num].find(' /')]
    requested_resource = strings[num][strings[num].find(' /'):strings[num].find(' HTTP/')]
    list_tuples.append((remote_addr, request_type, requested_resource))
    num += 1

print(list_tuples)