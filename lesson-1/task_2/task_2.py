"""Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""

import json
import requests

request_url = f'https://newsdata.io/api/1/news'
api_key = 'pub_2011767a92f53f94961636c2972fb1dc95f6f'
args = {
    'apikey': api_key,
    'country': 'us',
    'q': 'pizza',
}

response = requests.get(request_url, params=args)

with open('server_response.json', 'w+') as f:
    json.dump(json.loads(response.content), f, indent=4, ensure_ascii=False)
