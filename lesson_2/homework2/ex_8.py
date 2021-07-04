from json.decoder import JSONDecodeError
import requests
import time
import json

# 1
url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)  # запрос на получение токена
saved_answer1 = response.text  # сохраняем ответ
parsed_string_to_dict = json.loads(saved_answer1)  # переводим в словарь
element = "token"
element_seconds = "seconds"
if element and element_seconds in parsed_string_to_dict:  # делаем проверку на наличие ответа с токеном
    print("Токен найден")
else:
    print("ОШИБКА!Токен не найден")
get_token = parsed_string_to_dict[element]  # получаем токен в переменную из словаря
print(get_token)
get_seconds = parsed_string_to_dict[element_seconds]  # получаем время в секундах
print(get_seconds)

# 2
# Передаём token
response2 = requests.get(url, params={"token": get_token})
print("2: " + response2.text + " status code: " + str(response2.status_code))
assert response2.status_code == 200

saved_answer2 = response2.text  # сохраняем ответ
parsed_string_to_dict2 = json.loads(saved_answer2)  # переводим в словарь
status_find = "status"
if status_find in parsed_string_to_dict2:  # делаем проверку на наличие ответа с токеном
    print("Status найден")
else:
    print("ОШИБКА! Status не найден")
get_status = parsed_string_to_dict2[status_find]  # получаем токен в переменную из словаря
assert get_status == "Job is NOT ready"

# 3
time.sleep(get_seconds)

# 4
response3 = requests.get(url, params={"token": get_token})
# response3 = requests.post(url, cookies=token)
print("4: " + response3.text + " status code: " + str(response3.status_code))
assert response3.status_code == 200

saved_answer3 = response3.text  # сохраняем ответ
parsed_string_to_dict3 = json.loads(saved_answer3)  # переводим в словарь
if status_find in parsed_string_to_dict3:  # делаем проверку на наличие ответа с токеном
    print("Status2 найден")
else:
    print("ОШИБКА! Status2 не найден")
get_status2 = parsed_string_to_dict3[status_find]  # получаем токен в переменную из словаря
assert get_status2 == "Job is ready"
result_find = "result"
if result_find in parsed_string_to_dict3:  # делаем проверку на наличие ответа с токеном
    print("Result найден")
else:
    print("ОШИБКА! Result не найден")
get_result = parsed_string_to_dict3[result_find]
assert get_result is not None or ""








