import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserGet(BaseCase):
    # Zapusk v komandnoy stroke = cd <directoriya>
    # python -m pytest -s tests/test_user_get.py

    # неавторизованный запрос на данные - получаем только username
    def test_get_user_details_not_auth(self):
        # ID = 2
        response = MyRequests.get(url="user/2")

        Assertions.assert_json_has_key(response, "username")
        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response, expected_fields)

    # авторизованный запрос - авторизованы пользователем с ID 2 и делаем запрос для получения данных того же пользователя,
    # в этом случае мы получаем все поля
    def test_get_user_details_auth_as_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post(url="user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # Peredaem ID
        response2 = MyRequests.get(url=f"user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    # авторизовывается одним пользователем, но получает данные другого (т.е. с другим ID). И убедиться, что в этом случае
    # запрос также получает только username, так как мы не должны видеть остальные данные чужого пользователя.
    def test_get_user_details_auth_as_other_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post(url="user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        print(user_id_from_auth_method)

        # Передаём другой ID
        response2 = MyRequests.get(url=f"user/1",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_has_key(response2, "username")
        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response2, expected_fields)





