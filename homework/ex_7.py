from json.decoder import JSONDecodeError
import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# 1
response1 = requests.get(url)
parsed_response_text1 = response1.json()
print(parsed_response_text1)
print(response1.status_code)

# 2
response2 = requests.head(url, data={"method": "HEAD"})
parsed_response_text2 = response2.json()
print(parsed_response_text2)
print(response2.status_code)

# 3
response3 = requests.post(url, data={"method": "POST"})
parsed_response_text3 = response3.json()
print(parsed_response_text3)
print(response3.status_code)

# 4
parameters = ["GET", "POST", "PUT", "DELETE", "HEAD"]
for i in range(len(parameters)):
    url_get = requests.get(url, params={"method": parameters[i]})
    url_post = requests.post(url, data={"method": parameters[i]})
    url_put = requests.put(url, data={"method": parameters[i]})
    url_delete = requests.delete(url, data={"method": parameters[i]})
    url_head = requests.head(url, data={"method": parameters[i]})
    print('i = ', i, 'parameter = ', parameters[i], ' | ', url_get.text, ' | ', url_get.status_code, ' | ', url_post.text, ' | ', url_post.status_code, ' | ',
          url_put.text, ' | ', url_put.status_code, ' | ', url_delete.text, ' | ', url_delete.status_code, ' | ',  url_head.text, ' |', url_head.status_code)

# Подробная проверка
# GET
# url_0_1 = requests.get(url + "?method=GET")
# url_0_2 = requests.get(url + "?method=POST")
# url_0_3 = requests.get(url + "?method=PUT")
# url_0_4 = requests.get(url + "?method=DELETE")
# url_0_5 = requests.get(url + "?method=HEAD")
# print(url_0_1.text, '| ' + str(url_0_1.status_code))
# print(url_0_2.text, '| ' + str(url_0_2.status_code))
# print(url_0_3.text, '| ' + str(url_0_3.status_code))
# print(url_0_4.text, '| ' + str(url_0_4.status_code))
# print(url_0_5.text, '| ' + str(url_0_5.status_code))

#
# url_1_1 = requests.get(url, params={"method": "GET"})
# url_1_2 = requests.get(url, params={"method": "POST"})
# url_1_3 = requests.get(url, params={"method": "PUT"})
# url_1_4 = requests.get(url, params={"method": "DELETE"})
# url_1_5 = requests.get(url, params={"method": "HEAD"})
# print(url_1_1.text, '| ' + str(url_1_1.status_code))
# print(url_1_2.text, '| ' + str(url_1_2.status_code))
# print(url_1_3.text, '| ' + str(url_1_3.status_code))
# print(url_1_4.text, '| ' + str(url_1_4.status_code))
# print(url_1_5.text, '| ' + str(url_1_5.status_code))

# POST
# url_2_1 = requests.post(url, data={"method": "GET"})
# url_2_2 = requests.post(url, data={"method": "POST"})
# url_2_3 = requests.post(url, data={"method": "PUT"})
# url_2_4 = requests.post(url, data={"method": "DELETE"})
# url_2_5 = requests.post(url, params={"method": "HEAD"})
# print(url_2_1.text, '| ' + str(url_2_1.status_code))
# print(url_2_2.text, '| ' + str(url_2_2.status_code))
# print(url_2_3.text, '| ' + str(url_2_3.status_code))
# print(url_2_4.text, '| ' + str(url_2_4.status_code))
# print(url_2_5.text, '| ' + str(url_2_5.status_code))

# PUT
# url_3_1 = requests.put(url, data={"method": "GET"})
# url_3_2 = requests.put(url, data={"method": "POST"})
# url_3_3 = requests.put(url, data={"method": "PUT"})
# url_3_4 = requests.put(url, data={"method": "DELETE"})
# url_3_5 = requests.put(url, params={"method": "HEAD"})
# print(url_3_1.text, '| ' + str(url_3_1.status_code))
# print(url_3_2.text, '| ' + str(url_3_2.status_code))
# print(url_3_3.text, '| ' + str(url_3_3.status_code))
# print(url_3_4.text, '| ' + str(url_3_4.status_code))
# print(url_3_5.text, '| ' + str(url_3_5.status_code))

# DELETE
# url_4_1 = requests.delete(url, data={"method": "GET"})
# url_4_2 = requests.delete(url, data={"method": "POST"})
# url_4_3 = requests.delete(url, data={"method": "PUT"})
# url_4_4 = requests.delete(url, data={"method": "DELETE"})
# url_4_5 = requests.delete(url, params={"method": "HEAD"})
# print(url_4_1.text, '| ' + str(url_4_1.status_code))
# print(url_4_2.text, '| ' + str(url_4_2.status_code))
# print(url_4_3.text, '| ' + str(url_4_3.status_code))
# print(url_4_4.text, '| ' + str(url_4_4.status_code))
# print(url_4_5.text, '| ' + str(url_4_5.status_code))

# # HEAD
# url_5_1 = requests.head(url, data={"method": "GET"})
# url_5_2 = requests.head(url, data={"method": "POST"})
# url_5_3 = requests.head(url, data={"method": "PUT"})
# url_5_4 = requests.head(url, data={"method": "DELETE"})
# url_5_5 = requests.head(url, params={"method": "HEAD"})
# print(url_5_1.text, '| ' + str(url_5_1.status_code))
# print(url_5_2.text, '| ' + str(url_5_2.status_code))
# print(url_5_3.text, '| ' + str(url_5_3.status_code))
# print(url_5_4.text, '| ' + str(url_5_4.status_code))
# print(url_5_5.text, '| ' + str(url_5_5.status_code))
