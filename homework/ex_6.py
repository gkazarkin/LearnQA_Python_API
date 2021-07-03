from json.decoder import JSONDecodeError
import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
responses = response.history
number_response = len(responses)
print(number_response)
last_response = responses[-1]
print(last_response.url)

