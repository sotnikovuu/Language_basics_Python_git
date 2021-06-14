# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

f = open('nginx_logs.txt')
strings = f.readlines()
list_tuples = []
spammers_dictionary = {}
num = 0
while num <= len(strings) - 1:
    list_tuples.append(strings[num][:strings[num].find(' -')])
    spammers_dictionary.setdefault(list_tuples[num], 0)
    spammers_dictionary[list_tuples[num]] += 1
    num += 1
spammers_dictionary = sorted(spammers_dictionary.items(), key=lambda x: x[1])

print(spammers_dictionary[-5:])
