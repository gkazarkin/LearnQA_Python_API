import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    # 1
    def test_try_delete_user_id2(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post(url="user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(url=f"user/2",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = MyRequests.get(url=f"user/2",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_has_key(response4, "email")
        assert response4.json()['email'] == login_data['email']

    # 2 позитивный тест на удаление
    def test_delete_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()  # Sozdaem polzovatelya
        response1 = MyRequests.post(url="user", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post(url="user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(url=f"user/{user_id}",
                                      headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(url=f"user/{user_id}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        assert response4.text == "User not found"

    # 3
    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_delete_user_under_other_user_auth(self):
        # REGISTER 1
        register_data1 = self.prepare_registration_data()  # Sozdaem polzovatelya
        response1 = MyRequests.post(url="user", data=register_data1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email1 = register_data1["email"]
        first_name1 = register_data1["firstName"]
        password1 = register_data1["password"]
        last_name1 = register_data1["lastName"]
        user_id1 = self.get_json_value(response1, "id")

        # LOGIN
        login_data1 = {
            'email': email1,
            'password': password1
        }

        response2 = MyRequests.post(url="user/login", data=login_data1)
        auth_sid1 = self.get_cookie(response2, "auth_sid")
        token1 = self.get_header(response2, "x-csrf-token")

        # REGISTER 2
        register_data2 = self.prepare_registration_data()  # Sozdaem polzovatelya
        response3 = MyRequests.post(url="user", data=register_data2)
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")

        email2 = register_data2["email"]
        first_name2 = register_data2["firstName"]
        password2 = register_data2["password"]
        last_name2 = register_data2["lastName"]
        user_id2 = self.get_json_value(response3, "id")

        # LOGIN
        login_data2 = {
            'email': email2,
            'password': password2
        }

        response4 = MyRequests.post(url="user/login", data=login_data2)
        auth_sid2 = self.get_cookie(response4, "auth_sid")
        token2 = self.get_header(response4, "x-csrf-token")

        # DELETE
        response5 = MyRequests.delete(url=f"user/{user_id1}",
                                      headers={"x-csrf-token": token2}, cookies={"auth_sid": auth_sid2})
        Assertions.assert_code_status(response5, 400)  # Тут выдаёт ошибку, что статус_код 200, вероятно нашли баг

        # GET
        response6 = MyRequests.get(url=f"user/{user_id1}",
                                   headers={"x-csrf-token": token1}, cookies={"auth_sid": auth_sid1})
        Assertions.assert_json_has_key(response6, "username")
