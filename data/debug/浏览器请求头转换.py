import json

# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
referer: https://www.binancezh.top/service-worker.js
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
"""

# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')

# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers, indent=1, ensure_ascii=False))

# header = ""
# for i in headers:
#     if i == ':':
#         i = "\":\""
#     if i == '\n':
#         i = "\",\n\""
#     header += i
# print(header[2:])