import linecache
import time
import tkinter
import webbrowser
from tkinter import *
from tkinter import messagebox, colorchooser
from win32con import HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ
from requests.adapters import HTTPAdapter
import psutil
import requests
import win32gui
import win32event
import win32api
import sys
import os


class InfobarTool(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.d = None
        self.ckjb_i = 1
        self.ckjb = 1
        self.new_d1_Window_width = d1_Window_width
        self.net_text_first = psutil.net_io_counters()
        self.var_bgtm = IntVar(value=d1_bgtm_if)
        self.select = IntVar(value=d1_select_if)
        self.var_autokey = IntVar(value=d1_autokey)

        self.var_frm1 = IntVar(value=d1_frm1)
        self.var_frm2 = IntVar(value=d1_frm2)
        self.var_frm3 = IntVar(value=d1_frm3)

        self.title(version)
        # self.iconbitmap(r'D:\Python\InfobarTool\data\resources\images\logo.ico')  # 设置左上角图标，没有图片会报错
        self.geometry("-5000-5000")  # 例子：160x100+900+300，160x100为设置窗口尺寸，+900+300为设置窗口位置
        # self.geometry("182x40-1000+500")
        if d1_bgtm_if == 1:
            self.wm_attributes('-transparentcolor', d1_bg_color)  # 将d1_bg_color设置透明
        else:
            self.wm_attributes('-transparentcolor', '#796969')  # 将#796969色设置透明
        self.configure(bg=d1_bg_color)  # 设置窗体背景颜色
        # self.attributes('-alpha', 0.1)  # 设置窗体和控件透明度

        self.resizable(width=False, height=False)  # 给窗口设置横轴竖轴的可缩放性
        self.overrideredirect(True)  # 隐藏窗口边框和任务栏图标
        self.wm_attributes('-topmost', 1)  # 设置窗口置顶
        # self.attributes("-disabled", True)  # 可用"-toolwindow"（只显示关闭按钮）,"-fullscreen"（充满屏幕）,"-disabled"（不可点击）
        self.frm1 = Frame(self, bg=d1_bg_color, cursor='heart')
        self.frm2 = Frame(self, bg=d1_bg_color, cursor='heart')
        self.frm3 = Frame(self, bg=d1_bg_color, cursor='heart')

        self.l1 = Label(self.frm1, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="1")
        self.l2 = Label(self.frm1, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="1")
        self.l3 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="2")
        self.l4 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="2")
        self.l5 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="3")
        self.l6 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="3")

        self.frm1.pack(side='left', expand=YES, fill=BOTH)
        self.frm2.pack(side='left', expand=YES, fill=BOTH)
        self.frm3.pack(side='left', expand=YES, fill=BOTH)
        self.l1.pack(expand=YES, fill=Y)
        self.l2.pack(expand=YES, fill=Y)
        self.l3.pack(expand=YES, fill=Y)
        self.l4.pack(expand=YES, fill=Y)
        self.l5.pack(expand=YES, fill=Y)
        self.l6.pack(expand=YES, fill=Y)

        # 插入图片示例
        # image1 = PhotoImage(file='***.png')
        # label1 = Label(canvas, text="测试测试测试", image=image1, compound="center")
        # label1.pack(side='top', expand='yes')

        self.bind("<Button-3>", self.showmenu)
        self.update_btcdata()
        self.net()
        self.cpu_mem()
        self.window_to_taskbar()

    # tkinter控件显示逻辑
    def tk_show(self, function, text_v1, text_v2, font_v1, font_v2):
        def frm_forget():
            if self.var_frm1.get() == 0:
                self.frm1.pack_forget()
            if self.var_frm2.get() == 0:
                self.frm2.pack_forget()
            if self.var_frm3.get() == 0:
                self.frm3.pack_forget()

        if font_v1 == 0:
            font_v1 = ('等线', 10, 'bold')
        if font_v2 == 0:
            font_v2 = ('等线', 10, 'bold')
        if self.var_frm1.get() == function:
            self.frm1.pack_forget()
            self.frm2.pack_forget()
            self.frm3.pack_forget()
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
            frm_forget()
            self.l1.config(text=text_v1, font=font_v1)
            self.l2.config(text=text_v2, font=font_v2)
            self.l1.pack(expand=YES, fill=Y)
            self.l2.pack(expand=YES, fill=Y)
        if self.var_frm2.get() == function:
            self.frm1.pack_forget()
            self.frm2.pack_forget()
            self.frm3.pack_forget()
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
            frm_forget()
            self.l3.config(text=text_v1, font=font_v1)
            self.l4.config(text=text_v2, font=font_v2)
            self.l3.pack(expand=YES, fill=Y)
            self.l4.pack(expand=YES, fill=Y)
        if self.var_frm3.get() == function:
            self.frm1.pack_forget()
            self.frm2.pack_forget()
            self.frm3.pack_forget()
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
            frm_forget()
            self.l5.config(text=text_v1, font=font_v1)
            self.l6.config(text=text_v2, font=font_v2)
            self.l5.pack(expand=YES, fill=Y)
            self.l6.pack(expand=YES, fill=Y)

    # 网速信息获取
    def net(self):
        global runtime
        if 3 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:  # 首先先判断是否需要显示网速
            def formatnum(size):
                ds = ['', 'K', 'M', 'G', 'T']
                for d in ds:
                    if size < 1000:
                        if d:
                            return str(size) + d
                        else:
                            return f'{round(size / 1024, 1)}K'
                    size = round(size / 1024, 1)
                return '0B'

            net0 = self.net_text_first
            net1 = psutil.net_io_counters()
            net_sent = '上:%s' % formatnum((net1.bytes_sent - net0.bytes_sent) * 1)
            net_recv = '下:%s' % formatnum((net1.bytes_recv - net0.bytes_recv) * 1)
            self.net_text_first = psutil.net_io_counters()
            self.tk_show(3, net_sent, net_recv, 0, 0)
            runtime += 1
        else:
            runtime += 1
        self.after(998, self.net)  # 考虑程序执行延迟采用998毫秒

    # cpu和内存占用信息获取
    def cpu_mem(self):
        if 4 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
            cpu = f"核:%04.1f%%" % psutil.cpu_percent()  # 规定显示位数，不够用0占位
            mem = f"内:%04.1f%%" % psutil.virtual_memory().percent
            # cpu = f"CPU{psutil.cpu_percent()}%"
            # mem = f"内存{psutil.virtual_memory().percent}%"
            self.tk_show(4, cpu, mem, 0, 0)
        self.after(998, self.cpu_mem)

    # 虚拟货币实时价格信息获取
    def update_btcdata(self):
        global d1_select_if
        url = 'https://www.usd-cny.com/data/b.js'
        headers = {
            "Connection": "close",
            "User-Agent": "Edg/96.0.1054.62"
        }
        proxies = {'http': "http://127.0.0.1:10809",
                   'https': "http://127.0.0.1:10809"}
        requests.Session().mount('http://', HTTPAdapter(max_retries=2))
        requests.Session().mount('https://', HTTPAdapter(max_retries=2))  # 设置重试次数为2次
        try:
            try:
                response = requests.get(url=url, headers=headers)
                # response = json.loads(response.text)
                aa_list = response.text.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
                response.close()
                # print(aa_list[0])
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！')
            except Exception:
                response = requests.get(url=url, headers=headers, proxies=proxies)
                aa_list = response.text.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
                response.close()
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！使用v2ray代理端口')

            if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()] or \
                    2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:

                if d1_select_if == 1:
                    select_name = 'BTC'
                    data_list = aa_list[1].replace("\"", "").split(",")
                elif d1_select_if == 2:
                    select_name = 'ETH'
                    data_list = aa_list[2].replace("\"", "").split(",")
                else:
                    select_name = '币种出错'
                    data_list = []

                buy_btc = "%.1f" % float(data_list[8])
                high_btc = "%.0f" % float(data_list[6])
                low_btc = "%.0f" % float(data_list[7])
                base_btc = "%.1f" % float(data_list[5])
                # print(buy_btc + " " + high_btc + " " + low_btc + " " + base_btc)

                # 测试专用
                # buy_btc = "%.1f" % float(45000)
                # high_btc = "%.0f" % float(46000)
                # low_btc = "%.0f" % float(45500)
                # base_btc = "%.1f" % float(44000)

                add_btc = "%+.1f%%" % (((float(buy_btc) - float(base_btc)) / float(base_btc)) * 100)

                if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(1, (select_name+add_btc), ('$' + buy_btc), 0, 0)
                if 2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(2, ('高:' + high_btc), ('低:' + low_btc), 0, 0)
            else:
                print("单机模式，虚拟币数据已暂停获取")
                pass
        except Exception as err1:
            if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                self.tk_show(1, "无数据", "无数据", 0, 0)
            if 2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                self.tk_show(2, "无数据", "无数据", 0, 0)
            print(err1)
        self.after(5000, self.update_btcdata)  # 5秒钟执行一次该方法

    # 将窗口放置在任务栏并监控任务栏变化
    def window_to_taskbar(self):
        global d1_Window_width, b, d1_shiftx, d1_shiftx_new

        def Refresh(zck):
            global b
            if sys.getwindowsversion().build >= 22000:  # win11的内部版本号大于22000
                # 此判断目的是为了适配win11状态栏
                win32gui.SetParent(zck, m_hbar)  # 设置任务栏m_hBar为此窗口的父窗口
                if d1_shiftx > 500:  # 设置最右侧距离限制，否则重启软件会因为b数组变化出现显示位置错误
                    app.geometry(str(d1_Window_width) + 'x' + str(b[3] - b[1]) + '+' + str(d1_shiftx-500) + '+0')
                else:
                    appx = str(b[2] - b[0] - d1_Window_width - d1_shiftx)
                    app.geometry(str(d1_Window_width) + 'x' + str(b[3] - b[1]) + '+' + appx + '+0')
                    # 例子：160x100+X+Y，160x100为设置窗口尺寸，+X+Y为设置窗口位置，其中：
                    # +X表示距屏幕左边的距离X;-X表示距屏幕右边的距离X;+Y表示距屏幕上边的距离Y;-Y表示距屏幕下边的距离Y
                print('窗口移动成功(win11)')
            else:
                if d1_shiftx > 500:  # 设置最右侧距离限制，否则重启软件会因为b数组变化出现显示位置错误
                    # 将MSTaskSwWClass缩小[数字分别表示该窗口的左侧/顶部/右侧/底部坐标]，预留窗口位置，防止窗口被覆盖(对win11系统无效)
                    win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0], b[3] - b[1], True)
                    win32gui.SetParent(zck, m_hbar)  # 设置任务栏m_hBar为此窗口的父窗口
                    app.geometry(str(d1_Window_width) + 'x' + str(b[3] - b[1]) + '+' + str(d1_shiftx - 500) + '+0')
                else:
                    # 将MSTaskSwWClass缩小[数字分别表示该窗口的左侧/顶部/右侧/底部坐标]，预留窗口位置，防止窗口被覆盖(对win11系统无效)
                    win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0] - d1_Window_width - d1_shiftx, b[3] - b[1], True)
                    win32gui.SetParent(zck, m_hbar)  # 设置任务栏m_hBar为此窗口的父窗口
                    appx = str(b[2] - b[0] - d1_Window_width - d1_shiftx)
                    app.geometry(str(d1_Window_width) + 'x' + str(b[3] - b[1]) + '+' + appx + '+0')
                print('窗口移动成功(win10)')
            return 0

        try:
            #  将窗体放置于状态栏
            m_htaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
            m_hbar = win32gui.FindWindowEx(m_htaskbar, 0, "ReBarWindow32", None)
            m_hmin = win32gui.FindWindowEx(m_hbar, 0, "MSTaskSwWClass", None)
            ckjb_first = win32gui.FindWindow(None, version)  # 获取当前程序的窗口句柄
            c = win32gui.GetWindowRect(m_hbar)  # 获取m_hBar窗口尺寸为[左，上，右，下]的数组
            self.d = win32gui.GetWindowRect(m_hmin)  # 获取m_hmin窗口尺寸为[左，上，右，下]的数组
            if int(ckjb_first) != 0 and self.ckjb_i != 0:
                self.ckjb = ckjb_first
                self.ckjb_i = Refresh(ckjb_first)

            if c != b and d1_shiftx <= 500:  # 如果距托盘区距离超过500则不更新位置
                b = c
                Refresh(self.ckjb)

            elif d1_shiftx != d1_shiftx_new:
                d1_shiftx = d1_shiftx_new
                Refresh(self.ckjb)

            elif d1_Window_width != self.new_d1_Window_width:
                d1_Window_width = self.new_d1_Window_width
                Refresh(self.ckjb)
                save()

            else:
                pass

        except Exception as err2:
            print("获取当前窗口句柄失败!错误类型：" + str(err2))
        self.after(200, self.window_to_taskbar)

    # 右键菜单设置
    def showmenu(self, event):
        fmenu1 = Menu(self, tearoff=0)
        fmenu1.add_cascade(label="选择字体颜色", command=self.d1_word_color_diy)
        fmenu1.add_cascade(label="选择背景颜色", command=self.d1_bg_color_diy)
        fmenu1.add_checkbutton(label="透明背景", command=self.d1_bgtm_if_def, variable=self.var_bgtm)
        fmenu2 = Menu(self, tearoff=0)
        fmenu2.add_cascade(label="白底黑字(重启生效)", command=restore_b, background='#FFFFFF', foreground='#383838')
        fmenu2.add_cascade(label="黑底白字(重启生效)", command=restore_w, background='#383838', foreground='#FFFFFF')

        fmenu3 = Menu(self, tearoff=0)
        select_list = [
            ('BTC', 1),
            ('ETH', 2),
        ]
        for s_l, num in select_list:
            fmenu3.add_radiobutton(label=s_l, command=self.sz_pd, variable=self.select, value=num)

        fmenu4 = Menu(self, tearoff=0)
        fmenu5 = Menu(self, tearoff=0)
        fmenu6 = Menu(self, tearoff=0)
        select_list = [
            ('移除', 0),
            ('实时价格', 1),
            ('24H峰值', 2),
            ('网速显示', 3),
            ('CPU和内存占用', 4),
        ]
        for s_l, num in select_list:
            fmenu4.add_radiobutton(label=s_l, command=self.sz_pd, variable=self.var_frm1, value=num)
            fmenu5.add_radiobutton(label=s_l, command=self.sz_pd, variable=self.var_frm2, value=num)
            fmenu6.add_radiobutton(label=s_l, command=self.sz_pd, variable=self.var_frm3, value=num)

        menubar = Menu(self, tearoff=0)  # tearoff=0表示取消菜单独立，无横线
        menubar.add_cascade(label="第一功能区", menu=fmenu4)
        menubar.add_cascade(label="第二功能区", menu=fmenu5)
        menubar.add_cascade(label="第三功能区", menu=fmenu6)
        menubar.add_cascade(label="币种选择", menu=fmenu3)
        menubar.add_cascade(label="配色修改", menu=fmenu1)
        menubar.add_cascade(label="移动显示位置", command=self.move_position)
        menubar.add_separator()  # 添加菜单横线
        menubar.add_checkbutton(label="开机启动", command=autorun, variable=self.var_autokey)
        menubar.add_cascade(label="恢复默认", menu=fmenu2)
        menubar.add_cascade(label="程序说明", command=about)
        menubar.add_cascade(label="关闭程序", command=app_quit, background='#C8C8C8')

        menubar.post(event.x_root - 65, event.y_root - 50)
        print('右键菜单点击')

    # 是否选中判断
    def sz_pd(self):
        global d1_select_if, d1_frm1, d1_frm2, d1_frm3
        l_frm1 = self.var_frm1.get()
        l_frm2 = self.var_frm2.get()
        l_frm3 = self.var_frm3.get()
        list_frm = [l_frm1, l_frm2, l_frm3]
        if l_frm1 == 0:
            self.frm1.pack_forget()
        if l_frm2 == 0:
            self.frm2.pack_forget()
        if l_frm3 == 0:
            self.frm3.pack_forget()

        if list_frm.count(0) == 3:
            self.var_frm3.set(3)
            self.new_d1_Window_width = 70
            messagebox.showinfo(version, "不支持功能全关，已自动帮你打开仅显示网速模式\n\n另外：若是因修改配置文件导致该情况，重启即可恢复正常")
            save()
        if list_frm.count(0) == 2:
            self.new_d1_Window_width = 70
        if list_frm.count(0) == 1:
            self.new_d1_Window_width = 130
        if list_frm.count(0) == 0:
            self.new_d1_Window_width = 180

        d1_select_if = self.select.get()
        d1_frm1 = self.var_frm1.get()
        d1_frm2 = self.var_frm2.get()
        d1_frm3 = self.var_frm3.get()
        save()

    # 透明/有色背景判断函数
    def d1_bgtm_if_def(self):
        global d1_bgtm_if
        if d1_word_color == d1_bg_color:  # 防止背景和字体颜色相同
            messagebox.showwarning("警告", "背景和字体颜色不能相同")
        else:
            if self.var_bgtm.get() == 0:
                self.wm_attributes('-transparentcolor', '#796969')  # 将#796969色设置透明
            if self.var_bgtm.get() == 1:
                self.wm_attributes('-transparentcolor', d1_bg_color)  # 将d1_bg_color设置透明
        d1_bgtm_if = self.var_bgtm.get()
        save()

    # 字体颜色自定义函数
    def d1_word_color_diy(self):
        global d1_word_color
        color = colorchooser.askcolor()
        if color != (None, None):
            d1_word_color = str(color)[-9:-2]

        self.l1.config(fg=d1_word_color)
        self.l2.config(fg=d1_word_color)
        self.l3.config(fg=d1_word_color)
        self.l4.config(fg=d1_word_color)
        self.l5.config(fg=d1_word_color)
        self.l6.config(fg=d1_word_color)
        save()

    # 背景颜色自定义函数
    def d1_bg_color_diy(self):
        global d1_bg_color, d1_bgtm_if
        color = colorchooser.askcolor()
        # print(str(color)[-9:-2])
        if color != (None, None):
            d1_bg_color = str(color)[-9:-2]
        self.config(bg=d1_bg_color)
        self.frm1.config(bg=d1_bg_color)
        self.frm2.config(bg=d1_bg_color)
        self.frm3.config(bg=d1_bg_color)
        self.l1.config(bg=d1_bg_color)
        self.l2.config(bg=d1_bg_color)
        self.l3.config(bg=d1_bg_color)
        self.l4.config(bg=d1_bg_color)
        self.l5.config(bg=d1_bg_color)
        self.l6.config(bg=d1_bg_color)
        self.var_bgtm.set(0)
        save()

    # 移动滑块函数
    @staticmethod
    def move_position():
        def Show(val):
            global d1_shiftx_new
            d1_shiftx_new = int(val)

        def Reduce():
            s1.set(s1.get()-1)

        def Add():
            s1.set(s1.get()+1)

        def Left():
            s1.set(501)

        def Right():
            s1.set(0)

        def Close():
            save()
            movewindow.destroy()

        movewindow = Tk()
        if d1_shiftx >= 501:
            movewindow.geometry("+" + str(d1_shiftx - 500) + "+" + str(b[1] - 200))
        else:
            movewindow.geometry("+" + str(b[2] - b[0] - d1_Window_width - d1_shiftx) + "+" + str(b[1] - 200))
        # movewindow.resizable(width=False, height=False)  # 给窗口设置横轴竖轴的可缩放性
        movewindow.overrideredirect(True)  # 隐藏窗口边框和任务栏图标
        movewindow.wm_attributes('-alpha', 0.9)  # 设置窗口透明度
        movewindow.wm_attributes('-topmost', 1)  # 设置窗口置顶

        l1 = Label(movewindow, text="  拖动滑块改变位置  ", font=('微软雅黑', 12, 'bold'))
        s1 = Scale(movewindow, orient='horizontal', activebackground='red', troughcolor='#0080FF', font=('微软雅黑', 10),
                   sliderlength=20, sliderrelief='flat', relief='ridge', resolution=1, from_=0, to=1000, length=250,
                   command=Show)
        s1.set(d1_shiftx)
        frm1 = Frame(movewindow)
        Button(frm1, text="最左侧", font=('微软雅黑', 8), command=Left).pack(side='left', padx=10, pady=3)
        Button(frm1, text="-1", font=('微软雅黑', 8), command=Reduce).pack(side='left', padx=10, pady=3)
        Button(frm1, text="+1", font=('微软雅黑', 8), command=Add).pack(side='left', padx=10, pady=3)
        Button(frm1, text="最右侧", font=('微软雅黑', 8), command=Right).pack(side='left', padx=10, pady=3)
        l1.pack(pady=4)
        frm1.pack()
        s1.pack()
        Button(movewindow, text="关闭", font=('微软雅黑', 10, 'bold'), activeforeground='#0080FF', command=Close).pack(pady=5)


# 保存当前配置
def save():
    in_file = open(resource_path("%s.ini" % version), 'r', encoding='utf-8')
    out_file = open(resource_path("%s.ini" % version), 'r+', encoding='utf-8')
    index = 0

    dict_line = {4: d1_shiftx, 7: d1_bg_color, 10: d1_word_color, 13: d1_bgtm_if, 16: d1_frm3, 19: d1_select_if,
                 22: d1_Window_width, 25: d1_frm1, 28: d1_frm2, 31: d1_autokey}

    for line in in_file:
        index = index + 1
        if index in remove_line:
            out_file.write(str(dict_line[index]) + "\n")
        if index not in remove_line:
            out_file.write(line)

    in_file.close()
    out_file.close()
    print('保存配置成功')


# 退出函数，还原之前的状态栏窗口大小
def app_quit():
    if sys.getwindowsversion().build >= 22000:
        sys.exit()
    else:
        # 还原任务栏
        win32gui.MoveWindow(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindow(
            "Shell_TrayWnd", None), 0, "ReBarWindow32", None), 0, "MSTaskSwWClass", None), 0, 0, b[2]-b[0], b[3]-b[1], True)
        sys.exit()


# 定义一个读取相对路径的函数
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 程序说明函数
def about():
    root2 = tkinter.Toplevel()  # 两个窗口同时存在必须使用这个
    root2.title(version)
    root2.configure(bg='white')  # 设置窗体背景颜色
    root2.iconbitmap(resource_path(r'resources\images\logo.ico'))  # 设置图标，没有图片会报错

    curwidth = 900
    curhight = 760
    scn_w, scn_h = root2.maxsize()
    cen_x = (scn_w - curwidth) / 2
    cen_y = (scn_h - curhight) / 2
    size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
    root2.geometry(size_xy)
    root2.update()  # 设置窗体居中

    t = Text(root2, font=("微软雅黑", 10), bg="white")
    t.pack(side='top', expand=YES, fill=BOTH)
    t.insert("insert",
             "\n软件由MD制作，有问题请关注微信公众号：MD野生科技\n"
             "\n本次程序运行时长：%s秒\n"
             "\n软件已开源，地址(有可能被墙，请挂梯子访问)：https://github.com/mdmdwork/InfobarTool\n"
             "\n若您希望软件能持续更新、维护，还请打赏开发者，饮水思源，自愿打赏，不胜感激！\n\n"
             "XMR地址 \n"
             "4AZ8KJr9yXChs2Nk6KEyph5oKWC5oAPU3fWz7oTC6zCoL57oFHeyJm2NhbGx2N4eqDVZh7WbYbWmCjgzTfE5rnCSPqtF4gk\n\n"
             "BTC地址 \n"
             "1Kk4f7QDKTGhLgUgDzZhgidUJzFYJdoHgL\n\n"
             "ETC地址 \n"
             "0xaeefdfd30472d096d23f3a809d3d6bfe95ead0d4\n\n"
             "微信和支付宝二维码(推荐) \n" % str(runtime))
    t.tag_add("l", "1.0", "end")
    t.tag_config("l", justify="center")
    t.tag_add("link", "6.23", "6.69")
    t.tag_config("link", foreground="blue", underline=True)
    t.tag_add("link2", "2.0", "2.200")
    t.tag_config("link2", font=("黑体", 15, "bold"))
    t.tag_add("link3", "8.0", "8.200")
    t.tag_config("link3", font=("微软雅黑", 12, "bold"), foreground="red")
    t.tag_add("link4", "10.0", "10.200", "13.0", "13.200", "16.0", "16.200", "19.0", "19.200")
    t.tag_config("link4", font=("微软雅黑", 10, "bold"))

    def click(event):
        event.num = 0
        webbrowser.open("https://github.com/mdmdwork/InfobarTool")

    t.tag_bind("link", "<Button-1>", click)
    f1 = Frame(root2, bg='white', pady=20)
    photo1 = PhotoImage(file=resource_path(r'resources\images\wechat.gif'))
    photo2 = PhotoImage(file=resource_path(r'resources\images\alipay.gif'))
    p1 = Label(f1, image=photo1, width=250, height=250)
    p2 = Label(f1, image=photo2, width=250, height=250)
    p1.pack(side='left', padx=50)
    p2.pack(side='left', padx=50)
    t.window_create("insert", window=f1)
    root2.mainloop()
    root2.destroy()


# 白底黑字模式函数
def restore_b():
    # dict_line = {7: '#d5d5d5', 10: '#2b2b2b'}
    in_file = open(resource_path("%s.ini" % version), 'r', encoding='utf-8')
    out_file = open(resource_path("%s.ini" % version), 'r+', encoding='utf-8')
    index = 0
    dict_line = {7: '#d5d5d5', 10: '#2b2b2b'}

    for line in in_file:
        index = index + 1
        if index in [7, 10]:
            out_file.write(str(dict_line[index]) + "\n")
        if index not in [7, 10]:
            out_file.write(line)

    in_file.close()
    out_file.close()
    print('切换白底黑字模式，重启程序生效')
    # os.system(r"start " + version + ".exe")  # 通过cmd命令启动进程


# 黑底白字模式函数
def restore_w():
    out_file = open(resource_path("%s.ini" % version), 'w+', encoding='utf-8')
    r_w = ['这是配置文件，请勿胡乱修改！若因修改此文件导致软件异常，请删除本文件并重启！',
           '-------------------------------------------------------------',
           '##插入窗口距托盘区距离##d1_shiftx = ',
           '62',
           '-----------------------------',
           '##初始背景颜色##d1_bg_color = ',
           '#383838',
           '-----------------------------',
           '##初始字体颜色##d1_word_color = ',
           '#ffffff',
           '-----------------------------',
           '##透明背景##d1_bgtm_if = ',
           '1',
           '-----------------------------',
           '##第三功能区##d1_frm3 = ',
           '3',
           '-----------------------------',
           '##币种选择##d1_select_if =',
           '1',
           '-----------------------------',
           '##显示窗口宽度##d1_Window_width =',
           '180',
           '-----------------------------',
           '##第一功能区##d1_frm1 =',
           '1',
           '-----------------------------',
           '##第二功能区##d1_frm2 =',
           '4',
           '-----------------------------',
           '##开机自动启动##d1_autokey =',
           '0',
           '-----------------------------',
           ]
    for line in r_w:
        out_file.write(line + "\n")
    out_file.close()
    print('切换黑底白字模式，重启程序生效')


# 程序注册码函数
def zcm():
    global code_pd
    print("验证口令：" + code_pd)
    if code_pd == code_jm:
        return 1
    else:
        # 创建主窗口
        root = tkinter.Tk()
        root.title("初次启动验证")
        root.configure(bg='white')  # 设置窗体背景颜色
        root.iconbitmap(resource_path(r'resources\images\logo.ico'))  # 设置图标，没有图片会报错

        curwidth = 600
        curhight = 400
        scn_w, scn_h = root.maxsize()
        cen_x = (scn_w - curwidth) / 2
        cen_y = (scn_h - curhight) / 2
        size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
        root.geometry(size_xy)
        root.update()  # 窗体居中

        def zcm_def(ev=None):
            global code_pd
            result1 = e1.get()
            if str(result1) != code_jm:
                messagebox.showinfo("错误", "验证口令错误！请手动输入微信公众号名称！")
                # root.destroy()
                # sys.exit()

            if str(result1) == code_jm:
                out_file = open(resource_path("register.ini"), 'w+', encoding='utf-8')
                out_file.write(str(result1))
                out_file.close()
                root.destroy()
                code_pd = str(result1)

        l1 = Label(root, text="获取此软件更新请关注微信公众号：MD野生科技", font=('微软雅黑', 15, 'bold'), padx=0, pady=20, width=0, height=0, bg='white')
        photo = PhotoImage(file=resource_path(r'resources\images\MD_logo.gif'))
        p1 = Label(root, image=photo, width=200, height=200, bg='white')
        l2 = Label(root, text="请在下方文本框中手动输入：MD野生科技", font=('微软雅黑', 14), padx=0, pady=10, width=0, height=0, foreground='red', bg='white')
        f1 = Frame(root, bg='white')
        l3 = Label(f1, text="验证口令:", font=('微软雅黑', 15), padx=0, pady=0, borderwidth=0, width=0, height=0, bg='white')
        e1 = Entry(f1, font=('微软雅黑', 15), bg='white')
        e1.bind("<Return>", zcm_def)  # 监听回车键
        b1 = Button(root, text='确定', font=('微软雅黑', 12), width=5, height=1, command=zcm_def)
        l1.pack(side='top')
        p1.pack(side='top')
        l2.pack(side='top')
        f1.pack(side='top', expand=YES, fill=BOTH)
        l3.pack(side='left', padx=5)
        e1.pack(side='right', padx=10, expand=YES, fill=X)
        b1.pack(pady=10)
        root.mainloop()
        return 0


# 开机自启动注册表修改函数
def autorun():
    global d1_autokey
    name = 'InfobarTool'  # 要添加的项值名称
    path = resource_path(r'InfobarTool.exe')  # 要添加的exe路径
    runpath = r'Software\Microsoft\Windows\CurrentVersion\Run'  # 注册表路径
    if app.var_autokey.get() == 1:
        try:
            key = win32api.RegOpenKey(HKEY_CURRENT_USER, runpath, 0, KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, REG_SZ, path)
            win32api.RegCloseKey(key)
            messagebox.showinfo('提示', '开机启动注册表添加成功！')
        except Exception as erro:
            messagebox.showinfo('提示', '开机启动注册表添加失败！\n'+str(erro))

    if app.var_autokey.get() == 0:
        try:
            key = win32api.RegOpenKey(HKEY_CURRENT_USER, runpath, 0, KEY_ALL_ACCESS)
            win32api.RegDeleteValue(key, name)
            win32api.RegCloseKey(key)
            messagebox.showinfo('提示', '开机启动注册表已删除！')
        except Exception as erro:
            messagebox.showinfo('提示', '开机启动注册表删除失败！\n'+str(erro))
    d1_autokey = app.var_autokey.get()
    save()


if __name__ == '__main__':
    # 重复启动验证
    mutex = win32event.CreateMutex(None, False, 'InfobarTool_is_Running')
    if win32api.GetLastError() > 0:
        print('程序已启动')
        root1 = tkinter.Tk()
        root1.withdraw()
        root1.iconbitmap(resource_path(r'resources\images\logo.ico'))  # 设置图标，没有图片会报错
        messagebox.showinfo("打开失败", "程序已启动，请关闭或检查当前已启动的程序")
        sys.exit()
    # 初始化变量
    version = "InfobarTool_v1.0.7"
    code_jm = "MD野生科技"
    code_pd = linecache.getline(resource_path("register.ini"), 1).strip('\n')
    linecache.clearcache()
    remove_line = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
    b = win32gui.GetWindowRect(win32gui.FindWindowEx(win32gui.FindWindow("Shell_TrayWnd", None), 0, "ReBarWindow32", None))
    runtime = 0  # 程序运行起始时间

    # 验证口令
    if zcm() != 1 and code_pd != code_jm:
        sys.exit()

    try:
        file = open(resource_path("%s.ini" % version), 'r', encoding='utf-8')
        data1 = file.read().split("\n")  # 以换行符为分割点将数据分割为列表
        file.close()
        d1_shiftx = int(data1[remove_line[0] - 1])
        d1_bg_color = data1[remove_line[1] - 1]
        d1_word_color = data1[remove_line[2] - 1]
        d1_bgtm_if = int(data1[remove_line[3] - 1])
        d1_frm3 = int(data1[remove_line[4] - 1])
        d1_select_if = int(data1[remove_line[5] - 1])
        d1_Window_width = int(data1[remove_line[6] - 1])
        d1_frm1 = int(data1[remove_line[7] - 1])
        d1_frm2 = int(data1[remove_line[8] - 1])
        d1_autokey = int(data1[remove_line[9] - 1])
        d1_shiftx_new = d1_shiftx
        del data1

    except Exception as err:
        print(err)
        restore_w()
        file = open(resource_path("%s.ini" % version), 'r', encoding='utf-8')
        data1 = file.read().split("\n")  # 以换行符为分割点将数据分割为列表
        file.close()
        d1_shiftx = int(data1[remove_line[0] - 1])
        d1_bg_color = data1[remove_line[1] - 1]
        d1_word_color = data1[remove_line[2] - 1]
        d1_bgtm_if = int(data1[remove_line[3] - 1])
        d1_frm3 = int(data1[remove_line[4] - 1])
        d1_select_if = int(data1[remove_line[5] - 1])
        d1_Window_width = int(data1[remove_line[6] - 1])
        d1_frm1 = int(data1[remove_line[7] - 1])
        d1_frm2 = int(data1[remove_line[8] - 1])
        d1_autokey = int(data1[remove_line[9] - 1])
        d1_shiftx_new = d1_shiftx
        del data1

    app = InfobarTool()
    app.mainloop()
