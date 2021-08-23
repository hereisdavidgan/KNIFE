from urllib import request
url = r"http://www.baidu.com"
req = request.Request(url)  # 构造请求
response = request.urlopen(req).read().decode()  # 获取响应
print(response)
