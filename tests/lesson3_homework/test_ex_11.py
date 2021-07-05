import pytest
import requests
import json

def test_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"

    response = requests.get(url)
    print(response.text)  # No text
    response_as_dict = response.headers
    print(str(response_as_dict))
    cookie = dict(response_as_dict)["Set-Cookie"]
    print(cookie)
    expected_cookie1 = "HomeWork=hw_value"
    expected_cookie2 = "Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly"
    assert expected_cookie1 in cookie
    assert expected_cookie2 in cookie

    # Дополнительные проверки
    assert 'Set-Cookie' in response_as_dict, "There is no cookie"
    get_cookie = response.cookies.get('Set-Cookie')
    print(get_cookie)  # None

    assert 'Set-Cookie' in response.headers, "There is no Set-Cookie header in the response"
    get_header = response.headers.get('Set-Cookie')
    print(get_header)  # HomeWork=hw_value; expires=Thu, 05-Aug-2021 07:49:35 GMT; Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly



