# https://www.cnblogs.com/hsinfo/p/13618555.html
""" from urllib import request
url = r"http://www.baidu.com"
req = request.Request(url)  # 构造请求
response = request.urlopen(req).read().decode()  # 获取响应
print(response) """


from urllib import request
import re
headers = {
    "User-Agent": "Mozilla/5.0"
}
url = r"http://www.baidu.com"
req = request.Request(url, headers=headers)  # 构造请求
response = request.urlopen(req).read().decode()  # 获取响应
pat = r"<title>(.*?)</title>"  # 正则匹配规则
data = re.findall(pat, response)  # 正则匹配筛选
print(data)
