from json.decoder import JSONDecodeError
import requests

# 1
# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
parsed_response_text = response.json()
print("1: " + parsed_response_text["answer"])

# 2
response2 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response2.text)
try:
    parsed_response_text2 = response2.json()
    print("2: " + parsed_response_text2)
except JSONDecodeError:
    print("2: Response is not a JSON format")

# 3
# response3 = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# В POST надо не params, a data
response3 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print("3: " + response3.text)
print(response3.status_code)

# 4
response4 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response4.history[0]
second_response = response4
print("4: " + first_response.url)
print(second_response.url)
print(response4.status_code)

# 5
headers = {"some_header": "123"}
response5 = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print("5: Заголовки нашего запроса, которые получил сервер " + response5.text)
print("Заголовки ответа сервера " + str(response5.headers))

# 6 Получаем куки
payload2 = {"login": "secret_login", "password": "secret_pass"}
response6 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload2)
print("6: " + response6.text)
print(response6.status_code)
print(dict(response6.cookies))
print(response6.headers)

# 7 Передаём куки
# Берём куки
cookie_value = response6.cookies.get("auth_cookie")
# Создаём ключ-значение куки
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})
# Передаём куки
response7 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print("7: " + response7.text)
print(response7.status_code)
