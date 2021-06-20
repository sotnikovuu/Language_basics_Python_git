# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# #
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
import re


RE_NGINX = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                      r'.([0-9]{,3}\/[a-zA-Z]{,8}\/[0-9]{,4}\:[0-9]{,4}\:[0-9]{,4}\:[0-9]{,2} [+0-9]{,5})[]] \"'
                      r'([a-zA-Z]{,3}) (\/[a-z]{,10}\/[a-z0-9_]{,10}) [A-Z]{,6}\/[0-9]\.[0-9]\" ([0-9]{,3}) ([0-9]{,5}) \"-\" '
                      r'\"[a-zA-Z]{,10} [a-zA-Z0-9-/]{,10}\.[0-9] [(0-9]{,3}[.][0-9][.][0-9~A-Za-z]{,16}[.][0-9)]{,3}\"')

f = open('nginx_logs.txt')
while True:
    line = f.readline()
    for num_str in RE_NGINX.findall(line):
        remote_addr, request_datetime, request_type, requested_resource, response_code, response_size = num_str
    if not line:
        break
    print([remote_addr, request_datetime, request_type, requested_resource, response_code, response_size])

