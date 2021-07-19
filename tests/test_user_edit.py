import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
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

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(url=f"user/{user_id}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid}, data={"firstName": new_name})

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(url=f"user/{user_id}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    # Редактирование без авторизации
    def test_edit_created_user_without_auth(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(url="user", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed_Name"
        response2 = MyRequests.put(url=f"user/{user_id}", data={"firstName": new_name})

        Assertions.assert_code_status(response2, 400)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post(url="user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET
        response4 = MyRequests.get(url=f"user/{user_id}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_wrong_name(response4, "firstName", new_name, "Name of the user changed after edit without auth")

    # Редактирование под авторизованным другим пользователем
    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_edit_created_user_under_other_auth_user(self):
        # REGISTER
        register_data1 = self.prepare_registration_data()  # Sozdaem polzovatelya 1
        response1 = MyRequests.post(url="user", data=register_data1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email1 = register_data1["email"]
        first_name1 = register_data1["firstName"]
        password1 = register_data1["password"]
        last_name1 = register_data1["lastName"]
        user_id1 = self.get_json_value(response1, "id")

        register_data2 = self.prepare_registration_data()  # Sozdaem polzovatelya 2
        response2 = MyRequests.post(url="user", data=register_data2)
        print(response2.status_code)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email2 = register_data2["email"]
        first_name2 = register_data2["firstName"]
        password2 = register_data2["password"]
        last_name2 = register_data2["lastName"]
        user_id2 = self.get_json_value(response2, "id")

        # LOGIN 2
        login_data2 = {
            'email': email2,
            'password': password2
        }

        response3 = MyRequests.post(url="user/login", data=login_data2)
        auth_sid2 = self.get_cookie(response3, "auth_sid")
        token2 = self.get_header(response3, "x-csrf-token")

        # EDIT 1
        new_name = "Changed_Name"
        response4 = MyRequests.put(url=f"user/{user_id1}",
                                   headers={"x-csrf-token": token2}, cookies={"auth_sid": auth_sid2},
                                   data={"firstName": new_name})

        Assertions.assert_code_status(response4, 400)  # Тут выдаёт ошибку, что статус_код 200, вероятно нашли баг

        # LOGIN 1
        login_data1 = {
            'email': email1,
            'password': password1
        }

        response5 = MyRequests.post(url="user/login", data=login_data1)
        auth_sid1 = self.get_cookie(response5, "auth_sid")
        token1 = self.get_header(response5, "x-csrf-token")

        # GET
        response6 = MyRequests.get(url=f"user/{user_id1}",
                                   headers={"x-csrf-token": token1}, cookies={"auth_sid": auth_sid1})
        Assertions.assert_json_value_wrong_name(response6, "firstName", new_name, "Name of the user changed after edit under other user auth")

    # Авторизован, редактирование почты без @
    def test_edit_created_user_with_wrong_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(url="user", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_email = "testemail1.ru"
        response2 = MyRequests.put(url=f"user/{user_id}", data={"email": new_email})

        Assertions.assert_code_status(response2, 400)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post(url="user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET
        response4 = MyRequests.get(url=f"user/{user_id}",
                                   headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_wrong_email(response4, "email", new_email, "Email of the user changed after edit with wrong email without @")

    # Авторизован, редактирование на короткое имя
    def test_edit_created_user_with_short_name(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(url="user", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_username = "a"
        response2 = MyRequests.put(url=f"user/{user_id}", data={"username": new_username})

        Assertions.assert_code_status(response2, 400)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post(url="user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET
        response4 = MyRequests.get(url=f"user/{user_id}",
                                   headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        print(response4.text)
        Assertions.assert_json_value_wrong_name(response4, "username", new_username, "Name of the user changed after edit with very short name about 1 symbol")
