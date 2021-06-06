import datetime
from requests import get, utils


def currency_rates(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    exchange_rates = response.content.decode(encoding=encodings)
    if exchange_rates.count(f'<CharCode>{currency}</CharCode>') > 0:
        day_r, month_r, year_r = exchange_rates[exchange_rates.find('Date=') + 6:
                                                exchange_rates.find('name=')-2].split('.')
        date_request = datetime.date(year=int(year_r), month=int(month_r), day=int(day_r))

        exchange_rates = exchange_rates[exchange_rates.find(f'<CharCode>{currency}</CharCode>'):]
        exchange_rates = exchange_rates[(exchange_rates.find('<Value>') + 7):(exchange_rates.find('</Value>'))]
        exchange_rates = float(exchange_rates.replace(',', '.'))

        print(f'На {date_request} курс {currency} = {exchange_rates}')
        print(f'{currency} -', type(exchange_rates))
        print(f'{date_request} -', type(date_request))
    else:
        print('None')


if __name__ == '__main__':
    currency_rates('eur')
    currency_rates('usd')
