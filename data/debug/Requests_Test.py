import time
import requests
while True:
    url = 'http://www.usd-cny.com/data/b.js'
    headers = {
        "Connection": "close",
        "User-Agent": "Edg/96.0.1054.62"
    }
    proxies = {'http': "http://127.0.0.1:10809",
               'https': "http://127.0.0.1:10809"}
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
    except Exception as err1:
        response = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)
    response.enconding = "utf-8"
    aa_list = response.text.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
    print(aa_list)
    data_list = aa_list[0].replace("var hq_str_btc_btcbtcusd=", "").replace("\"", "").split(",")
    # print(data_list)

    hbbuy = "%.1f" % float(data_list[8])
    hbhigh = "%.1f" % float(data_list[6])
    hblow = "%.1f" % float(data_list[7])
    hbc = "%.1f%%" % (((float(hbhigh) - float(hblow)) / float(hblow)) * 100)

    btc1 = hbbuy
    btc2 = '▼' + hblow
    btc3 = '▲' + hbhigh
    btc4 = '今日振幅：' + hbc
    print(btc1+" "+btc2+" "+btc3+" "+btc4)
    time.sleep(1)
