import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    # 4tobi zapustit test otdelno:
    # cd <directoriya>
    # python -m pytest -s test/test_user_register.py -k test_create_user_successfully

    exclude_params = [
        ("no_email"),
        ("no_username"),
        ("no_firstname"),
        ("no_lastname"),
        ("no_password")
    ]

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

    # Homework
    # 1
    def test_create_user_with_wrong_email(self):
        email = "testexample.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post(url="user/", data=data)

        Assertions.assert_code_status(response, 400)
        print(response.status_code)
        print(response.content)
        assert response.content.decode(
            "utf-8") == 'Invalid email format'

    # 2
    @pytest.mark.parametrize("exclude", exclude_params)
    def test_create_user_without_any_field(self, exclude):
        if exclude == "no_email":
            email = ""
            data1 = self.prepare_registration_data(email)
            response = MyRequests.post(url="user/", data=data1)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'email' field is too short"
        elif exclude == "no_username":
            username = ""
            data2 = self.prepare_registration_data(username)
            response = MyRequests.post(url="user/", data=data2)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'email' field is too short"  # Здесь конечно странный ответ сервера
        elif exclude == "no_firstname":
            firstname = ""
            data3 = self.prepare_registration_data(firstname)
            response = MyRequests.post(url="user/", data=data3)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'email' field is too short"  # Здесь конечно странный ответ сервера
        elif exclude == "no_lastname":
            lastname = ""
            data4 = self.prepare_registration_data(lastname)
            response = MyRequests.post(url="user/", data=data4)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'email' field is too short"  # Здесь конечно странный ответ сервера
        elif exclude == "no_password":
            password = ""
            data5 = self.prepare_registration_data(password)
            response = MyRequests.post(url="user/", data=data5)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'email' field is too short"  # Здесь конечно странный ответ сервера

    # 3
    def test_create_user_with_short_name(self):
        username = "a"
        data = self.prepare_registration_data(username)

        response = MyRequests.post(url="user/", data=data)

        Assertions.assert_code_status(response, 400)
        print(response.status_code)
        print(response.content)

        assert response.content.decode(
            "utf-8") == "The value of 'email' field is too short"

    # 4
    def test_create_user_with_verylong_name(self):
        username = "qwertyuiopasdfghjklzxcvbnmgopshgwohgwpoghwopughwpoghwopghwoghwopghwgowhgopwuhgpowuhgpouahgopwauhgwaopughwapoughwapoughwapoguhwpoguhwgpouwahgpowuh" \
                   "gwpoughwarpoughwarpoughwaropughwarpoughwarepoguwhreagpouwarehgowruaehgwproaughwopughwarpoughwpoguihwhgpwoa"
        data = self.prepare_registration_data(username)

        response = MyRequests.post(url="user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "The value of 'email' field is too long"




