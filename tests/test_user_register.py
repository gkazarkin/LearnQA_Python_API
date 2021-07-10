import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    # 4tobi zapustit test otdelno:
    # cd <directoriya>
    # python -m pytest -s test/test_user_register.py -k test_create_user_successfully

    def test_create_user_succesfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post(url="user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post(url="user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
        print(response.status_code)
        print(response.content)  # b - Означает, что это инфа в форме байт, а не текста (нужно декодировать в utf-8)
