import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    csrf_token_variable = "x-csrf-token"
    auth_sid_variable = "auth_sid"
    user_id_variable = "user_id"

    def setup(self):
        self.url1 = "https://playground.learnqa.ru/api/user/login"
        self.url2 = "https://playground.learnqa.ru/api/user/auth"


        self.data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        # 1
        response1 = requests.post(self.url1, data=self.data)

        self.auth_sid = self.get_cookie(response1, self.auth_sid_variable)
        self.token = self.get_header(response1, self.csrf_token_variable)
        self.user_id_from_auth_method = self.get_json_value(response1, self.user_id_variable)

    # Positive test
    def test_auth_user(self):
        # 2
        response2 = requests.get(self.url2, headers={self.csrf_token_variable: self.token}, cookies={self.auth_sid_variable: self.auth_sid})

        Assertions.assert_json_value_by_name(response2, self.user_id_variable, self.user_id_from_auth_method, "User id from auth method is not equal to user id from check method")

    # Negative test
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_user(self, condition):
        # 1
        response1 = requests.post(self.url1, data=self.data)
        assert self.auth_sid_variable in response1.cookies, "There is no auth cookies in the response1"
        assert self.csrf_token_variable in response1.headers, "There is no csrf-token header in the response1"
        assert self.user_id_variable in response1.json(), "There is no user id in the response1"

        auth_sid = response1.cookies.get(self.auth_sid_variable)
        token = response1.headers.get(self.csrf_token_variable)

        if condition == "no_cookie":
            response2 = requests.get(
                self.url2, headers={self.csrf_token_variable: token}
            )
        else:
            response2 = requests.get(
                self.url2, cookies={self.auth_sid_variable: auth_sid}
            )

        Assertions.assert_json_value_by_name(response2, self.user_id_variable, 0,
                                             f"User authorised with condition {condition}")
