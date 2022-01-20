import tkinter
from tkinter import *
import webbrowser

root = tkinter.Tk()
root.title("11")
root.configure(bg='white')  # 设置窗体背景颜色
root.iconbitmap(r'D:\Python\InfobarTool\data\resources\images\MD_logo.gif')  # 设置图标，没有图片会报错
runtime = 100
curwidth = 780
curhight = 670
scn_w, scn_h = root.maxsize()
cen_x = (scn_w - curwidth) / 2
cen_y = (scn_h - curhight) / 2
size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
root.geometry(size_xy)
root.update()  # 设置窗体居中

t = Text(root, font=("微软雅黑", 10), width=600, height=10)
t.pack(side='top', expand=YES, fill=BOTH)
t.insert("insert",
         "\n软件由MD野生科技—信仰之名制作，有问题请关注微信公众号：MD野生科技\n"
         "\n本次程序运行时长：%s秒\n"
         "\n软件已开源，地址(有可能被墙，请挂梯子访问)：https://github.com/mdmdwork/InfobarTool\n"
         "\n若您希望软件能持续更新、维护，还请捐赠开发者，饮水思源，自愿捐赠，不胜感激！\n\n"
         "XMR地址: \n"
         "4AZ8KJr9yXChs2Nk6KEyph5oKWC5oAPU3fWz7oTC6zCoL57oFHeyJm2NhbGx2N4eqDVZh7WbYbWmCjgzTfE5rnCSPqtF4gk\n\n"
         "BTC地址: \n"
         "1Kk4f7QDKTGhLgUgDzZhgidUJzFYJdoHgL\n\n"
         "ETC地址: \n"
         "0xaeefdfd30472d096d23f3a809d3d6bfe95ead0d4\n\n"
         "微信和支付宝二维码(推荐): \n" % str(runtime - 10))
t.tag_add("link", "6.23", "6.69")
t.tag_config("link", foreground="blue", underline=True)
t.tag_add("link2", "2.0", "2.200")
t.tag_config("link2", justify="center", font=("黑体", 14))
t.tag_add("link3", "8.0", "8.200")
t.tag_config("link3", justify="center", font=("微软雅黑", 12, "bold"), foreground="red")
t.tag_add("link4", "10.0", "10.200", "13.0", "13.200", "16.0", "16.200", "19.0", "19.200")
t.tag_config("link4", font=("微软雅黑", 10, "bold"))


def click(event):
    webbrowser.open("https://github.com/mdmdwork/InfobarTool")


t.tag_bind("link", "<Button-1>", click)
f1 = Frame(root, bg='white')
photo1 = PhotoImage(file=r'D:\Python\InfobarTool\data\resources\images\wechat.gif')
photo2 = PhotoImage(file=r'D:\Python\InfobarTool\data\resources\images\alipay.gif')
p1 = Label(f1, image=photo1, width=250, height=250, bg='white')
p2 = Label(f1, image=photo2, width=250, height=250, bg='white')
f1.pack(side='top')
p1.pack(side='left', padx=60, pady=10)
p2.pack(side='left', padx=60, pady=10)
root.mainloop()
