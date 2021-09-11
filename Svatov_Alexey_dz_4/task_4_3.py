import requests
from datetime import datetime
import requests.utils as utils


def currency_rates(main_valute):
    def separate(str, border):
        mean = str[str.find(border) + len(border):valute.find(border[0] + '/' + border[1:])]
        if ',' in mean:
            return float(mean.replace(',', '.'))
        return mean

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    head_info, main_info = str(content.split('<Valute ')[:1]), content.split('<Valute ')[1:]
    dict_info = {}
    date = head_info[head_info.find('Date="') + len('Date="'):head_info.find('Date="') + len('Date="') + 10]
    for valute in main_info:
        dict_info.setdefault(separate(valute, '<CharCode>'), separate(valute, '<Value>'))

    return print(f"{dict_info.get(main_valute): .2f}, {datetime.strptime(date, '%d.%m.%Y').date()}")


if __name__ == '__main__':
    print('Main file')
