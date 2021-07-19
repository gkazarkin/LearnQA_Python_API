from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expeced_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expeced_value, error_message

    @staticmethod
    def assert_json_value_wrong_name(response: Response, name, expeced_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] != expeced_value, error_message

    @staticmethod
    def assert_json_value_wrong_email(response: Response, email, expeced_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert email in response_as_dict, f"Response JSON doesn't have key '{email}'"
        assert response_as_dict[email] != expeced_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    # Proveryaem spisok zna4eniy
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it is present"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it is present"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected:  {expected_status_code}. Actual: {response.status_code}"



