import pytest
import requests
import json

def test_header():
    url = "https://playground.learnqa.ru/api/homework_header"

    response = requests.get(url)
    print(response.text)
    response_as_dict = response.headers
    print(str(response_as_dict))

    expected_header_1_1 = "x-secret-homework-header"
    expected_header_1_2 = "Some secret value"
    assert expected_header_1_1 in response.headers, "There is no 'x-secret-homework-header' header in the response"
    secret_header = dict(response_as_dict)["x-secret-homework-header"]
    print(secret_header)
    assert expected_header_1_2 in secret_header, "There is no 'Some secret value' of header in the response"
