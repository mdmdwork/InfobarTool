import hashlib
import time
import win32api


def encode_sct(code_cp):
    code_jm1 = str(code_cp)*2 + '加密@2021'
    m = hashlib.md5()
    m.update(code_jm1.encode("utf8"))
    code_jm2 = m.hexdigest()

    return code_jm2


number = win32api.GetVolumeInformation("C:\\")[1]
print("本机机器码：" + str(number))
print("本机注册码：" + encode_sct(str(number)))

code_cp = input("输入明文：")
print("密文是：", encode_sct(code_cp))
time.sleep(600)
