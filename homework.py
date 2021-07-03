# import requests
import json
from json.decoder import JSONDecodeError

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# Парсим строку в объект
obj = json.loads(json_text)

key = "messages"
if key in obj:
    print(obj[key][1])
else:
    print(f"Ключа {key} в JSON нет")

