import linecache
import time
import tkinter
from tkinter import *
from tkinter import messagebox, colorchooser
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
        self.ckjb_i = 1
        self.ckjb = 1
        self.new_d1_Window_width = d1_Window_width
        self.net_text_first = psutil.net_io_counters()
        self.var1 = IntVar(value=d1_bgtm_if)
        self.select = IntVar(value=d1_select_if)

        self.var_frm1 = IntVar(value=d1_frm1)
        self.var_frm2 = IntVar(value=d1_frm2)
        self.var_frm3 = IntVar(value=d1_frm3)

        self.title(version)
        # self.iconbitmap('logo.ico')  # 设置左上角图标，没有图片会报错
        self.geometry("-5000-5000")  # 例子：160x100+900+300，160x100为设置窗口尺寸，+900+300为设置窗口位置
        # self.geometry("182x40+500+500")
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
                        font=('等线', 10, 'bold'), text="虚拟币种类")
        self.l2 = Label(self.frm1, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="实时价格")
        self.l3 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="24H高价")
        self.l4 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="24H低价")
        self.l5 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="上传速度")
        self.l6 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=d1_word_color, bg=d1_bg_color,
                        font=('等线', 10, 'bold'), text="下载速度")

        # 插入图片示例
        # image1 = PhotoImage(file='***.png')
        # label1 = Label(canvas, text="测试测试测试", image=image1, compound="center")
        # label1.pack(side='top', expand='yes')

        self.bind("<Button-3>", self.showmenu)
        self.update_btcdata2()
        self.net_if()
        self.cpu_mem()
        self.window_to_taskbar()
        self.windows2()

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
    def net_if(self):
        if 3 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:  # 首先先判断是否需要显示网速
            def formatnum(size):
                ds = ['', 'k', 'm', 'g', 't']
                for d in ds:
                    if size < 1000:
                        if d:
                            return str(size) + d + "/s"
                        else:
                            return f'{round(size / 1024, 1)}k/s'
                    size = round(size / 1024, 1)
                return '0b/s'

            net0 = self.net_text_first
            net1 = psutil.net_io_counters()
            net_sent = '⇡%s' % formatnum((net1.bytes_sent - net0.bytes_sent) * 1)
            net_recv = '⇣%s' % formatnum((net1.bytes_recv - net0.bytes_recv) * 1)
            self.net_text_first = psutil.net_io_counters()
            self.tk_show(3, net_sent, net_recv, 0, 0)
        else:
            pass
        self.after(995, self.net_if)  # 考虑程序执行延迟采用995毫秒

    # cpu和内存占用信息获取
    def cpu_mem(self):
        if 4 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
            cpu = f"CPU%04.1f%%" % psutil.cpu_percent()  # 规定显示位数，不够用0占位
            mem = f"内存%04.1f%%" % psutil.virtual_memory().percent
            # cpu = f"CPU{psutil.cpu_percent()}%"
            # mem = f"内存{psutil.virtual_memory().percent}%"
            self.tk_show(4, cpu, mem, 0, 0)
        self.after(995, self.cpu_mem)

    @staticmethod
    def update_btcdata():
        url = 'https://www.usd-cny.com/data/b.js'
        headers = {
            "Connection": "close",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
        }
        proxies = {'http': "http://127.0.0.1:10809",
                   'https': "http://127.0.0.1:10809"}
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=2))
        s.mount('https://', HTTPAdapter(max_retries=2))  # 设置重试次数为2次

        try:
            response = s.get(url=url, headers=headers)
            # response = json.loads(response.text)
            aa = response.text
            # print(aa[0])
            aa_list = aa.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
            # print(aa_list[0])
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！')
        except Exception as err3:
            response = s.get(url=url, headers=headers, proxies=proxies)
            aa = response.text + str(err3)  # 为了消除pycharm警告....
            aa_list = aa.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！使用v2ray代理端口')
        return aa_list

    def update_btcdata2(self):
        global d1_select_if
        if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()] or \
                2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
            try:
                aa_list = self.update_btcdata()
                if d1_select_if == 1:
                    select_name = 'BTC'
                    data_list = aa_list[0].replace("var hq_str_btc_btcbtcusd=", "").replace("\"", "").split(",")
                    # print(data_list)
                elif d1_select_if == 2:
                    select_name = 'ETH'
                    data_list = aa_list[2].replace("var hq_str_btc_btcethusd=", "").replace("\"", "").split(",")
                else:
                    select_name = '币种出错'
                    data_list = []

                buy_btc = "%.1f" % float(data_list[8])
                high_btc = "%.0f" % float(data_list[6])
                low_btc = "%.0f" % float(data_list[7])
                base_btc = "%.1f" % float(data_list[5])

                # 测试专用
                # buy_btc = "%.1f" % float(45000)
                # high_btc = "%.0f" % float(46000)
                # low_btc = "%.0f" % float(45500)
                # base_btc = "%.1f" % float(44000)

                add_btc = "%+.1f%%" % (((float(buy_btc) - float(base_btc)) / float(base_btc)) * 100)

                if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(1, (select_name + ' ' + add_btc), ('$ ' + buy_btc), 0, 0)
                if 2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(2, ('⇡' + high_btc), ('⇣' + low_btc), 0, 0)
            except Exception as err1:
                if 1 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(1, "无数据", "无数据", 0, 0)
                if 2 in [self.var_frm1.get(), self.var_frm2.get(), self.var_frm3.get()]:
                    self.tk_show(2, "无数据", "无数据", 0, 0)
                print(err1)
        else:
            print("单机模式，虚拟币数据已暂停获取")
            pass
        self.after(5000, self.update_btcdata2)  # 5秒钟执行一次该方法

    # 将窗口放置在任务栏并监控任务栏变化
    def window_to_taskbar(self):
        global d1_Window_width, b, d1_shiftx, d1_shiftx_new

        def Refresh(zck):
            win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0] - d1_Window_width - d1_shiftx, b[3] - b[1],
                                True)  # 将MSTaskSwWClass缩小[x位置，y位置，宽，高]，预留窗口位置
            win32gui.SetParent(zck, m_hbar)  # 设置任务栏m_hBar为此窗口的父窗口
            appx = str(b[2] - b[0] - d1_Window_width - d1_shiftx)
            widthy = b[3] - b[1]  # 插入窗口的高
            app.geometry(str(d1_Window_width) + 'x' + str(widthy) + '+' + appx + '+0')
            print('窗口移动成功')
            return 0

        try:
            #  将窗体放置于状态栏
            m_htaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
            m_hbar = win32gui.FindWindowEx(m_htaskbar, 0, "ReBarWindow32", None)
            m_hmin = win32gui.FindWindowEx(m_hbar, 0, "MSTaskSwWClass", None)
            ckjb_first = win32gui.FindWindow(None, version)  # 获取当前程序的窗口句柄
            if int(ckjb_first) != 0 and self.ckjb_i != 0:
                self.ckjb = ckjb_first
                self.ckjb_i = Refresh(ckjb_first)

            c = win32gui.GetWindowRect(m_hbar)  # 获取m_hBar窗口尺寸b为[左，上，右，下]的数组

            if c != b:
                b = c
                Refresh(self.ckjb)

            elif d1_shiftx != d1_shiftx_new:
                d1_shiftx = d1_shiftx_new
                Refresh(self.ckjb)

            elif d1_Window_width != self.new_d1_Window_width:
                d1_Window_width = self.new_d1_Window_width
                Refresh(self.ckjb)
                self.save()

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
        fmenu1.add_checkbutton(label="透明背景", command=self.d1_bgtm_if_def, variable=self.var1)
        fmenu2 = Menu(self, tearoff=0)
        fmenu2.add_cascade(label="白底黑字", command=restore_b, background='#FFFFFF', foreground='#383838')
        fmenu2.add_cascade(label="黑底白字", command=restore_w, background='#383838', foreground='#FFFFFF')

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

        # fmenu4 = Menu(self, tearoff=0)
        # fmenu4.add_checkbutton(label="实时价格", command=self.sz_pd, variable=self.var2)
        # fmenu4.add_checkbutton(label="24H峰值", command=self.sz_pd, variable=self.var3)
        # fmenu4.add_checkbutton(label="网速显示", command=self.sz_pd, variable=self.var4)

        menubar = Menu(self, tearoff=0)  # tearoff=0表示取消菜单独立，无横线
        menubar.add_cascade(label="币种选择", menu=fmenu3)
        menubar.add_cascade(label="配色修改", menu=fmenu1)
        menubar.add_cascade(label="第一功能区", menu=fmenu4)
        menubar.add_cascade(label="第二功能区", menu=fmenu5)
        menubar.add_cascade(label="第三功能区", menu=fmenu6)
        menubar.add_cascade(label="移动此工具位置", command=self.move_position)
        menubar.add_separator()  # 添加菜单横线
        menubar.add_cascade(label="恢复默认", menu=fmenu2)
        menubar.add_cascade(label="程序说明", command=self.about)
        menubar.add_cascade(label="关闭程序", command=self.app_quit, background='#C8C8C8')

        menubar.post(event.x_root - 65, event.y_root - 30)
        print('右键菜单点击')

    # 退出函数，还原之前的状态栏窗口大小
    def app_quit(self):
        win32gui.MoveWindow(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindow(
            "Shell_TrayWnd", None), 0, "ReBarWindow32", None), 0, "MSTaskSwWClass", None),
            0, 0, b[2] - b[0] - d1_shiftx, b[3] - b[1], True)  # 还原任务栏
        self.quit()

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
        if list_frm.count(0) == 2:
            self.new_d1_Window_width = 70
        if list_frm.count(0) == 1:
            self.new_d1_Window_width = 130
        if list_frm.count(0) == 0:
            self.new_d1_Window_width = 180

        d1_select_if = self.select.get()
        d1_frm1 = l_frm1
        d1_frm2 = l_frm2
        d1_frm3 = l_frm3
        self.save()

    # 透明/有色背景判断函数
    def d1_bgtm_if_def(self):
        global d1_bgtm_if
        if d1_word_color == d1_bg_color:  # 防止背景和字体颜色相同
            messagebox.showwarning("警告", "背景和字体颜色不能相同")
        else:
            if d1_bgtm_if == 1:
                self.wm_attributes('-transparentcolor', '#796969')  # 将#796969色设置透明
                d1_bgtm_if = 0
            else:
                self.wm_attributes('-transparentcolor', d1_bg_color)  # 将d1_bg_color设置透明
                d1_bgtm_if = 1
        self.save()

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
        self.save()

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
        d1_bgtm_if = 0
        self.save()

    # 移动滑块函数
    def move_position(self):
        def show(val):
            global d1_shiftx_new
            d1_shiftx_new = int(val)

        def close():
            self.save()
            root.destroy()

        root = Tk()
        root.geometry("+" + str(b[2] - b[0] - (int(d1_Window_width / 1.8)) - d1_shiftx) + "+" + str(b[1] - 150))
        root.resizable(width=False, height=False)  # 给窗口设置横轴竖轴的可缩放性
        root.overrideredirect(True)  # 隐藏窗口边框和任务栏图标
        root.wm_attributes('-alpha', 0.7)  # 设置窗口透明度

        l1 = Label(root, text="  拖动滑块改变位置  ", font=('微软雅黑', 12, 'bold'))
        l1.pack()
        s1 = Scale(root, orient='horizontal', activebackground='red', troughcolor='#0080FF', font=('微软雅黑', 10),
                   sliderlength=20, sliderrelief='flat', relief='ridge', resolution=1, from_=0, to=500, length=200,
                   command=show)
        s1.set(d1_shiftx)
        s1.pack()
        Button(root, text="关闭", font=('微软雅黑', 10, 'bold'), activeforeground='#0080FF', command=close).pack()

    # 保存当前配置
    @staticmethod
    def save():
        in_file = open("%s.ini" % version, 'r', encoding='utf-8')
        out_file = open("%s.ini" % version, 'r+', encoding='utf-8')
        index = 0

        dict_line = {4: d1_shiftx, 7: d1_bg_color, 10: d1_word_color, 13: d1_bgtm_if, 16: d1_frm3, 19: d1_select_if,
                     22: d1_Window_width,
                     25: d1_frm1, 28: d1_frm2}

        for line in in_file:
            index = index + 1
            if index in remove_line:
                out_file.write(str(dict_line[index]) + "\n")
            if index not in remove_line:
                out_file.write(line)

        in_file.close()
        out_file.close()
        print('保存配置成功')

    # 程序说明函数
    @staticmethod
    def about():
        root = tkinter.Tk()
        root.title(version)
        root.configure(bg='white')  # 设置窗体背景颜色

        curwidth = 550
        curhight = 350
        scn_w, scn_h = root.maxsize()
        cen_x = (scn_w - curwidth) / 2
        cen_y = (scn_h - curhight) / 2
        size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
        root.geometry(size_xy)
        root.update()  # 设置窗体居中

        t = tkinter.Text(root)
        t.pack()
        t.insert("insert", "\n该软件由MD野生科技—信仰之名制作，有问题请关注微信公众号：MD野生科技\n\n"
                           "或联系邮箱mdwork@163.com\n\n"
                           "-----------------------------------------------------------------------\n\n"
                           "该软件为个人开发，耗费大量精力，若您希望软件能持续更新、维护，还请捐赠开发者!\n\n"
                           "饮水思源，自愿捐赠，不胜感激！虚拟货币钱包地址：\n\n"
                           "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤\n"
                           "XMR(推荐)：\n"
                           "4AZ8KJr9yXChs2Nk6KEyph5oKWC5oAPU3fWz7oTC6zCoL57oFHeyJm2NhbGx2N4eqDVZh7WbYbWmCjgzTfE5rnCSPqtF4gk\n\n"
                           "BTC(0.00005个起付)：\n"
                           "1Kk4f7QDKTGhLgUgDzZhgidUJzFYJdoHgL\n\n"
                           "ETC(0.01个起付)：\n"
                           "0xaeefdfd30472d096d23f3a809d3d6bfe95ead0d4\n"
                           "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤\n\n"
                           "本次程序运行时长：" + str(runtime - 10) + "秒\n\n")
        tkinter.Button(root, text=" 关闭 ", command=root.destroy).pack()
        # root.mainloop()

    # 60秒调整一次任务栏窗口，防止长时间不移动主窗体被覆盖
    def windows2(self):
        global runtime
        try:
            m_htaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
            m_hbar = win32gui.FindWindowEx(m_htaskbar, 0, "ReBarWindow32", None)
            m_hmin = win32gui.FindWindowEx(m_hbar, 0, "MSTaskSwWClass", None)
            win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0] - d1_Window_width - d1_shiftx, b[3] - b[1],
                                True)  # 将MSTaskSwWClass缩小[x位置，y位置，宽，高]，预留窗口位置

            print('程序运行时间:' + str(runtime) + '秒')
        except Exception as err3:
            print('程序运行时间:' + str(runtime) + '秒\n' + str(err3))
        runtime = runtime + 60
        self.after(60000, self.windows2)


# 定义一个读取相对路径的函数
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 白底黑字模式函数
def restore_b():
    # dict_line = {7: '#d5d5d5', 10: '#2b2b2b'}
    in_file = open("%s.ini" % version, 'r', encoding='utf-8')
    out_file = open("%s.ini" % version, 'r+', encoding='utf-8')
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
    out_file = open("%s.ini" % version, 'w+', encoding='utf-8')
    r_w = ['这是配置文件，请勿胡乱修改！若因修改此文件导致软件异常，请恢复默认文件！',
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
           '-----------------------------'
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
        root.iconbitmap(resource_path(r'resources\images\logo.ico'))  # 设置图标，没有图片会报错

        curwidth = 400
        curhight = 200
        scn_w, scn_h = root.maxsize()
        cen_x = (scn_w - curwidth) / 2
        cen_y = (scn_h - curhight) / 2
        size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
        root.geometry(size_xy)
        root.update()  # 窗体居中

        def zcm_def():
            global code_pd
            result1 = e1.get()
            if str(result1) != code_jm:
                messagebox.showinfo("错误", "验证口令错误！请手动输入微信公众号名称！")
                # root.destroy()
                # sys.exit()

            if str(result1) == code_jm:
                out_file = open("register.ini", 'w+', encoding='utf-8')
                out_file.write(str(result1))
                out_file.close()
                root.destroy()
                code_pd = str(result1)

        l1 = Label(root, text="获取此软件更新请关注微信公众号：MD野生科技", font=('微软雅黑', 12), padx=0, pady=10, width=0, height=0)
        l1.pack(side='top')
        l2 = Label(root, text="请在下部文本框中手动输入微信公众号名称", font=('微软雅黑', 12), padx=0, pady=10, width=0, height=0)
        l2.pack(side='top')

        f1 = Frame(root)
        l2 = Label(f1, text="验证口令:", font=('微软雅黑', 12), padx=0, pady=0, borderwidth=0, width=0, height=0)
        e1 = Entry(f1, font=('微软雅黑', 12))
        f1.pack(side='top', expand=YES, fill=BOTH)
        l2.pack(side='left', padx=5)
        e1.pack(side='left', padx=10, expand=YES, fill=X)

        b1 = Button(root, text='确定', font=('微软雅黑', 12), width=5, height=1, command=zcm_def)
        b1.pack(pady=10)
        root.mainloop()
        return 0


if __name__ == '__main__':
    # 重复启动验证
    mutex = win32event.CreateMutex(None, False, 'InfobarTool_is_Running')
    if win32api.GetLastError() > 0:
        print('程序已启动')
        root1 = tkinter.Tk()
        root1.withdraw()
        messagebox.showinfo("打开失败", "程序已启动，请关闭或检查当前已启动的程序")
        sys.exit()
    # 初始化变量
    version = "InfobarTool_v1.0.2"
    code_jm = "MD野生科技"
    code_pd = linecache.getline("register.ini", 1).strip('\n')
    linecache.clearcache()
    remove_line = [4, 7, 10, 13, 16, 19, 22, 25, 28]
    b = win32gui.GetWindowRect(win32gui.FindWindowEx(win32gui.FindWindow("Shell_TrayWnd", None), 0, "ReBarWindow32", None))
    runtime = 0  # 程序运行起始时间

    # 验证口令
    if zcm() != 1 and code_pd != code_jm:
        sys.exit()

    try:
        d1_shiftx = int(linecache.getline("%s.ini" % version, remove_line[0]).replace(" ", "").strip('\n'))  # 去掉空格，去换行符
        d1_bg_color = linecache.getline("%s.ini" % version, remove_line[1]).replace(" ", "").strip('\n')
        d1_word_color = linecache.getline("%s.ini" % version, remove_line[2]).replace(" ", "").strip('\n')
        d1_bgtm_if = int(linecache.getline("%s.ini" % version, remove_line[3]).replace(" ", "").strip('\n'))
        d1_frm3 = int(linecache.getline("%s.ini" % version, remove_line[4]).replace(" ", "").strip('\n'))
        d1_select_if = int(linecache.getline("%s.ini" % version, remove_line[5]).replace(" ", "").strip('\n'))
        d1_Window_width = int(linecache.getline("%s.ini" % version, remove_line[6]).replace(" ", "").strip('\n'))
        d1_frm1 = int(linecache.getline("%s.ini" % version, remove_line[7]).replace(" ", "").strip('\n'))
        d1_frm2 = int(linecache.getline("%s.ini" % version, remove_line[8]).replace(" ", "").strip('\n'))
        d1_shiftx_new = d1_shiftx

    except Exception as err:
        print(err)
        restore_w()
        linecache.clearcache()  # linecach重复读取，不清理的话会直接从缓存中读取
        d1_shiftx = int(linecache.getline("%s.ini" % version, remove_line[0]).replace(" ", "").strip('\n'))  # 去掉空格，去换行符
        d1_bg_color = linecache.getline("%s.ini" % version, remove_line[1]).replace(" ", "").strip('\n')
        d1_word_color = linecache.getline("%s.ini" % version, remove_line[2]).replace(" ", "").strip('\n')
        d1_bgtm_if = int(linecache.getline("%s.ini" % version, remove_line[3]).replace(" ", "").strip('\n'))
        d1_frm3 = int(linecache.getline("%s.ini" % version, remove_line[4]).replace(" ", "").strip('\n'))
        d1_select_if = int(linecache.getline("%s.ini" % version, remove_line[5]).replace(" ", "").strip('\n'))
        d1_Window_width = int(linecache.getline("%s.ini" % version, remove_line[6]).replace(" ", "").strip('\n'))
        d1_frm1 = int(linecache.getline("%s.ini" % version, remove_line[7]).replace(" ", "").strip('\n'))
        d1_frm2 = int(linecache.getline("%s.ini" % version, remove_line[8]).replace(" ", "").strip('\n'))
        d1_shiftx_new = d1_shiftx

    app = InfobarTool()
    app.mainloop()
