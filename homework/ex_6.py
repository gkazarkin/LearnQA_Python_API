from json.decoder import JSONDecodeError
import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
responses = response.history
number_response = len(responses)
redirects = number_response - 1
print(redirects)
last_response = responses[-1]
print(last_response.url)

# print(responses[0].url)
# print(responses[1].url)
# print(responses[2].url)
# print(responses[3].url)
