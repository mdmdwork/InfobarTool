import os
import sys
import tkinter
from tkinter import messagebox

# 定义一个读取相对路径的函数
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = tkinter.Tk()
root.withdraw()
root.iconbitmap(r'D:\Python\InfobarTool\data\resources\images\logo.ico')  # 设置图标，没有图片会报错
messagebox.showinfo('1', '2')