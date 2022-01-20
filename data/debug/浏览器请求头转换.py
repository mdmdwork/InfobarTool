import json

# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control: max-age=0
if-modified-since: Thu, 20 Jan 2022 06:42:05 GMT
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62
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