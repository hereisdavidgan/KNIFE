
import requests
print('Hello World')

url = "https://www.baidu,com"
data = '{"id":"utf-8"}'
# 字符串格式
res = requests.post(url=url,data=data)
print(res.text)

