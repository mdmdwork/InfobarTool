import re
import requests


url = 'https://www.usd-cny.com/data/b.js'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
proxies = {'http': "http://127.0.0.1:10809",
           'https': "http://127.0.0.1:10809"}
try:
    response = requests.get(url=url, headers=headers)
except Exception as err1:
    response = requests.get(url=url, headers=headers, proxies=proxies)

# response = json.loads(response.text)
response.encoding = response.apparent_encoding
aa = response.text
print(aa)
aa_list = aa.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
print(aa_list[0])
data_list = aa_list[0].replace("var hq_str_btc_btcbtcusd=", "").replace("\"", "").split(",")
print(data_list)

hbbuy = "%.1f" % float(data_list[8])
hbhigh = "%.1f" % float(data_list[6])
hblow = "%.1f" % float(data_list[7])
hbc = "%.1f%%" % (((float(hbhigh) - float(hblow)) / float(hblow)) * 100)

btc1 = hbbuy
btc2 = '▼' + hblow
btc3 = '▲' + hbhigh
btc4 = '今日振幅：' + hbc
print(btc1+" "+btc2+" "+btc3+" "+btc4)
