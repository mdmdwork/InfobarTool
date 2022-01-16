import tkinter as tk
from tkinter import ttk
from tkinter import *


root = tk.Tk()
root.title("测试")
transparentcolor = "red"
# root.wm_attributes('-transparentcolor', transparentcolor)
# root.configure(bg='green')
# l1 = ttk.Label(root, foreground="black", background="red", font=('等线', 200, 'bold'), text="123456789")
# l1.pack(fill=X)
# l2 = ttk.Label(root, foreground="red", background="black", font=('等线', 200, 'bold'), text="123456789")
# l2.pack()
#
# l3 = ttk.Label(root, background='white', font=('等线', 10, 'bold'), text="123456789")
# Label(root, bitmap="hourglass").pack()


radio1 = ttk.Checkbutton(root, text="111")
radio1.pack()
radio2 = tk.Checkbutton(root, text="222")
radio2.pack()
menubar = tk.Menu(root)
root.config(menu=menubar)
menu1 = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="语言", menu=menu1)
menu1.add_checkbutton(label="汉语")
menu1.add_checkbutton(label="英语")
menu2 = tk.Menu(menubar, tearoff=False)
menu2.add_checkbutton(label="red")
menu2.add_checkbutton(label="blue")
menubar.add_cascade(label="颜色", menu=menu2)

root.mainloop()