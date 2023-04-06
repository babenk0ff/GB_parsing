"""Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json."""

import json
import requests

response = requests.get('https://api.github.com/users/babenk0ff/repos')

full_data = json.loads(response.text)
repo_list = [repo['name'] for repo in full_data]

with open('github_parse.json', 'w+') as f:
    json.dump(repo_list, f, indent=4)
