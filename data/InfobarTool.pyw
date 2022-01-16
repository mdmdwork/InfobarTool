import tkinter.colorchooser
import tkinter.simpledialog
from tkinter import *
from tkinter import messagebox
from psutil import net_io_counters
from requests.adapters import HTTPAdapter
import tkinter
import requests
import win32gui
import linecache
import time


class InfobarTool(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.ckjb_i = 1
        self.ckjb = 1
        self.var1 = IntVar(value=bgpd)
        self.var2 = IntVar(value=d1_ssjg)
        self.var3 = IntVar(value=d1_24hfz)
        self.var4 = IntVar(value=netpd)
        self.net1 = net_io_counters()
        self.select = IntVar(value=select_pd)

        self.title(version)
        # self.iconbitmap('logo.ico')  # 设置左上角图标，没有图片会报错
        self.geometry("180x40-5000-5000")  # 例子：160x100+900+300，160x100为设置窗口尺寸，+900+300为设置窗口位置
        # self.geometry("165x40+500+500")
        if bgpd == 1:
            self.wm_attributes('-transparentcolor', bg_color)  # 将bg_color设置透明
        else:
            self.wm_attributes('-transparentcolor', '#796969')  # 将#796969色设置透明
        self.configure(bg=bg_color)  # 设置窗体背景颜色
        # self.attributes('-alpha', 0.1)  # 设置窗体和控件透明度

        self.resizable(width=False, height=False)  # 给窗口设置横轴竖轴的可缩放性
        self.overrideredirect(True)  # 隐藏窗口边框和任务栏图标
        self.wm_attributes('-topmost', 1)  # 设置窗口置顶

        # self.attributes("-disabled", True)  # 可用"-toolwindow"（只显示关闭按钮）,"-fullscreen"（充满屏幕）,"-disabled"（不可点击）

        self.frm1 = Frame(self, bg=bg_color, padx=0, pady=0, borderwidth=0, width=0, height=0, cursor='heart')
        # self.frm1.pack(side='left', expand=YES, fill=BOTH)
        self.frm2 = Frame(self, bg=bg_color, padx=0, pady=0, borderwidth=0, width=0, height=0, cursor='heart')
        # self.frm2.pack(side='left', expand=YES, fill=BOTH)
        self.frm3 = Frame(self, bg=bg_color, padx=0, pady=0, borderwidth=0, width=0, height=0, cursor='heart')
        # self.frm3.pack(side='left', expand=YES, fill=BOTH)

        self.l1 = Label(self.frm1, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 10, 'bold'), text="虚拟币种类")
        self.l2 = Label(self.frm1, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 13, 'bold'), text="实时价格")
        self.l3 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 10, 'bold'), text="24H高价")
        self.l4 = Label(self.frm2, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 10, 'bold'), text="24H低价")
        self.l5 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 10, 'bold'), text="上传速度")
        self.l6 = Label(self.frm3, padx=0, pady=0, borderwidth=0, width=0, height=0, fg=word_color, bg=bg_color,
                        font=('等线', 10, 'bold'), text="下载速度")

        # 插入图片示例
        # image1 = PhotoImage(file='***.png')
        # label1 = Label(canvas, text="测试测试测试", image=image1, compound="center")
        # label1.pack(side='top', expand='yes')

        self.bind("<Button-3>", self.showmenu)
        self.netpd()
        self.update_btcdata2()
        self.mainpd()
        self.windows2()

    # tkinter显示逻辑
    def mainpd(self):
        global d1_ckkd, netpd, b, shiftx, shiftx_new

        def all_pack():
            self.frm1.pack_forget()
            self.frm2.pack_forget()
            self.frm3.pack_forget()
            self.l1.pack(expand=YES, fill=Y)
            self.l2.pack(expand=YES, fill=Y)
            self.l3.pack(expand=YES, fill=Y)
            self.l4.pack(expand=YES, fill=Y)
            self.l5.pack(expand=YES, fill=Y)
            self.l6.pack(expand=YES, fill=Y)

        if [d1_ssjg, d1_24hfz, netpd] == [0, 0, 1]:
            all_pack()
            new_d1_ckkd = 80
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [0, 1, 0]:
            all_pack()
            new_d1_ckkd = 80
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [1, 0, 0]:
            all_pack()
            new_d1_ckkd = 80
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [1, 1, 0]:
            all_pack()
            new_d1_ckkd = 130
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [0, 1, 1]:
            all_pack()
            new_d1_ckkd = 130
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [1, 0, 1]:
            all_pack()
            new_d1_ckkd = 130
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
        elif [d1_ssjg, d1_24hfz, netpd] == [1, 1, 1]:
            all_pack()
            new_d1_ckkd = 181
            self.frm1.pack(side='left', expand=YES, fill=BOTH)
            self.frm2.pack(side='left', expand=YES, fill=BOTH)
            self.frm3.pack(side='left', expand=YES, fill=BOTH)
        else:
            netpd = 1
            new_d1_ckkd = 80
            self.var4.set(1)
            self.save()
            messagebox.showinfo(version, "不支持功能全关，已自动帮你打开仅显示网速模式\n\n另外：若是因修改配置文件导致该情况，重启即可恢复正常")

        def Refresh(zck):
            win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0] - d1_ckkd - shiftx, b[3] - b[1],
                                True)  # 将MSTaskSwWClass缩小[x位置，y位置，宽，高]，预留窗口位置
            win32gui.SetParent(zck, m_hbar)  # 设置任务栏m_hBar为此窗口的父窗口
            appx = str(b[2] - b[0] - d1_ckkd - shiftx)
            widthy = b[3] - b[1]  # 插入窗口的高
            app.geometry(str(d1_ckkd) + 'x' + str(widthy) + '+' + appx + '+0')
            print('窗口移动成功')
            return 0

        try:
            # # 将窗体放置于状态栏
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

            elif shiftx != shiftx_new:
                shiftx = shiftx_new
                Refresh(self.ckjb)

            elif d1_ckkd != new_d1_ckkd:
                d1_ckkd = new_d1_ckkd
                Refresh(self.ckjb)
                self.save()

            else:
                pass

        except Exception as err2:
            print("获取当前窗口句柄失败!错误类型：" + str(err2))
        self.after(200, self.mainpd)

    # 网速信息获取
    def netpd(self):
        # print("网速显示" + str(netpd))
        if netpd == 1:  # 首先先判断是否需要显示网速
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

            net0 = self.net1
            net1 = net_io_counters()
            self.l5.config(text='⇡' + formatnum((net1.bytes_sent - net0.bytes_sent) * 1))
            self.l6.config(text='⇣' + formatnum((net1.bytes_recv - net0.bytes_recv) * 1))
            self.net1 = net_io_counters()
        else:
            pass
        self.after(995, self.netpd)  # 考虑程序执行延迟采用995毫秒

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
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！')
        except Exception:
            response = s.get(url=url, headers=headers, proxies=proxies)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 数据更新成功！使用v2ray代理端口')

        # response = json.loads(response.text)
        aa = response.text
        # print(aa[0])
        aa_list = aa.replace("\n", "").split(";")  # 将换行符号替换为空，并按；分割为列表
        # print(aa_list[0])
        return aa_list

    def update_btcdata2(self):
        global select_pd
        if d1_ssjg == 1 or d1_24hfz == 1:
            try:
                aa_list = self.update_btcdata()
                if select_pd == 1:
                    select_name = 'BTC'
                    data_list = aa_list[0].replace("var hq_str_btc_btcbtcusd=", "").replace("\"", "").split(",")
                    # print(data_list)
                elif select_pd == 2:
                    select_name = 'ETH'
                    data_list = aa_list[2].replace("var hq_str_btc_btcethusd=", "").replace("\"", "").split(",")
                else:
                    select_name = '币种出错'
                    data_list = []

                buy_btc = "%.1f" % float(data_list[8])
                high_btc = "%.0f" % float(data_list[6])
                low_btc = "%.0f" % float(data_list[7])
                base_btc = "%.1f" % float(data_list[5])
                if buy_btc > base_btc:
                    add_btc = "+%.1f%%" % (((float(buy_btc) - float(base_btc)) / float(base_btc)) * 100)
                else:
                    add_btc = "%.1f%%" % (((float(buy_btc) - float(base_btc)) / float(base_btc)) * 100)

                if d1_ssjg == 1:
                    self.l1.config(text=select_name + ' ' + add_btc)
                    self.l2.config(text='$'+buy_btc)
                else:
                    pass

                if d1_24hfz == 1:
                    self.l3.config(text='⇡' + high_btc)
                    self.l4.config(text='⇣' + low_btc)
                else:
                    pass
            except Exception as err1:
                self.l1.config(text='无数据', font=('等线', 10, 'bold'))
                self.l2.config(text='无数据', font=('等线', 10, 'bold'))
                self.l3.config(text='无数据', font=('等线', 10, 'bold'))
                self.l4.config(text='无数据', font=('等线', 10, 'bold'))
                print(err1)
        else:
            print("单网速模式，虚拟币数据已暂停获取")
            pass
        self.after(5000, self.update_btcdata2)  # 5秒钟执行一次该方法

    # 右键菜单设置
    def showmenu(self, event):
        fmenu1 = Menu(self, tearoff=0)
        fmenu1.add_cascade(label="选择字体颜色", command=self.word_color_diy)
        fmenu1.add_cascade(label="选择背景颜色", command=self.bg_color_diy)
        fmenu1.add_checkbutton(label="透明背景", command=self.bgpd_def, variable=self.var1)
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
        fmenu4.add_checkbutton(label="实时价格", command=self.sz_pd, variable=self.var2)
        fmenu4.add_checkbutton(label="24H峰值", command=self.sz_pd, variable=self.var3)
        fmenu4.add_checkbutton(label="网速显示", command=self.sz_pd, variable=self.var4)

        menubar = Menu(self, tearoff=0)  # tearoff=0表示取消菜单独立，无横线
        menubar.add_cascade(label="币种选择", menu=fmenu3)
        menubar.add_cascade(label="配色修改", menu=fmenu1)
        menubar.add_cascade(label="选择显示信息", menu=fmenu4)
        menubar.add_cascade(label="移动此工具位置", command=self.move_position)
        menubar.add_separator()  # 添加菜单横线
        # menubar.add_cascade(label="设置", command=self.setting)
        menubar.add_cascade(label="恢复默认", menu=fmenu2)
        menubar.add_cascade(label="程序说明", command=self.about)
        menubar.add_cascade(label="关闭程序", command=self.quit, background='#C8C8C8')

        menubar.post(event.x_root-65, event.y_root-30)
        print('右键菜单点击')

    # 设置菜单函数
    # @staticmethod
    # def setting():
    #     messagebox.showinfo("MD野生科技", "开发中")

    # 是否选中判断
    def sz_pd(self):
        global select_pd, d1_ssjg, d1_24hfz, netpd
        select_pd = self.select.get()
        d1_ssjg = self.var2.get()
        d1_24hfz = self.var3.get()
        netpd = self.var4.get()
        self.save()

    # 透明/有色背景判断函数
    def bgpd_def(self):
        global bgpd
        if word_color == bg_color:  # 防止背景和字体颜色相同
            messagebox.showwarning("警告", "背景和字体颜色不能相同")
        else:
            if bgpd == 1:
                self.wm_attributes('-transparentcolor', '#796969')  # 将#796969色设置透明
                bgpd = 0
            else:
                self.wm_attributes('-transparentcolor', bg_color)  # 将bg_color设置透明
                bgpd = 1
        self.save()

    # 字体颜色自定义函数
    def word_color_diy(self):
        global word_color
        color = tkinter.colorchooser.askcolor()
        if color != (None, None):
            word_color = str(color)[-9:-2]

        self.l1.config(fg=word_color)
        self.l2.config(fg=word_color)
        self.l3.config(fg=word_color)
        self.l4.config(fg=word_color)
        self.l5.config(fg=word_color)
        self.l6.config(fg=word_color)
        self.save()

    # 背景颜色自定义函数
    def bg_color_diy(self):
        global bg_color, bgpd
        color = tkinter.colorchooser.askcolor()
        # print(str(color)[-9:-2])
        if color != (None, None):
            bg_color = str(color)[-9:-2]
        self.config(bg=bg_color)
        self.frm1.config(bg=bg_color)
        self.frm2.config(bg=bg_color)
        self.frm3.config(bg=bg_color)
        self.l1.config(bg=bg_color)
        self.l2.config(bg=bg_color)
        self.l3.config(bg=bg_color)
        self.l4.config(bg=bg_color)
        self.l5.config(bg=bg_color)
        self.l6.config(bg=bg_color)
        bgpd = 0
        self.save()

    # 移动滑块函数
    def move_position(self):
        def show(val):
            global shiftx_new
            shiftx_new = int(val)

        def close():
            self.save()
            root.destroy()

        root = Tk()
        root.geometry("+" + str(b[2] - b[0] - (int(d1_ckkd / 1.8)) - shiftx) + "+" + str(b[1] - 150))
        root.resizable(width=False, height=False)  # 给窗口设置横轴竖轴的可缩放性
        root.overrideredirect(True)  # 隐藏窗口边框和任务栏图标
        root.wm_attributes('-alpha', 0.7)  # 设置窗口透明度

        l1 = Label(root, text="  拖动滑块改变位置  ", font=('微软雅黑', 12, 'bold'))
        l1.pack()
        s1 = Scale(root, orient='horizontal', activebackground='red', troughcolor='#0080FF', font=('微软雅黑', 10),
                   sliderlength=20, sliderrelief='flat', relief='ridge', resolution=1, from_=0, to=500, length=200,
                   command=show)
        s1.set(shiftx)
        s1.pack()
        Button(root, text="关闭", font=('微软雅黑', 10, 'bold'), activeforeground='#0080FF', command=close).pack()

    # 保存当前配置
    @staticmethod
    def save():
        in_file = open("%s.ini" % version, 'r', encoding='utf-8')
        out_file = open("%s.ini" % version, 'r+', encoding='utf-8')
        index = 0

        dict_line = {4: shiftx, 7: bg_color, 10: word_color, 13: bgpd, 16: netpd, 19: select_pd, 22: d1_ckkd,
                     25: d1_ssjg, 28: d1_24hfz}

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
            win32gui.MoveWindow(m_hmin, 0, 0, b[2] - b[0] - d1_ckkd - shiftx, b[3] - b[1],
                                True)  # 将MSTaskSwWClass缩小[x位置，y位置，宽，高]，预留窗口位置

            print('程序运行时间:' + str(runtime) + '秒')
        except Exception as err3:
            print('程序运行时间:' + str(runtime) + '秒\n' + str(err3))
        runtime = runtime + 60
        self.after(60000, self.windows2)


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
           '##插入窗口距托盘区距离##shiftx = ',
           '62',
           '-----------------------------',
           '##初始背景颜色##bg_color = ',
           '#383838',
           '-----------------------------',
           '##初始字体颜色##word_color = ',
           '#ffffff',
           '-----------------------------',
           '##透明背景##bgpd = ',
           '1',
           '-----------------------------',
           '##网速显示##netpd = ',
           '1',
           '-----------------------------',
           '##币种选择##select_pd =',
           '1',
           '-----------------------------',
           '##显示窗口宽度##d1_ckkd =',
           '181',
           '-----------------------------',
           '##实时价格##d1_ssjg =',
           '1',
           '-----------------------------',
           '##24H峰值##d1_24hfz =',
           '1',
           '-----------------------------'
           ]
    for line in r_w:
        out_file.write(line + "\n")
    out_file.close()
    print('切换黑底白字模式，重启程序生效')


'''程序注册码函数'''


def zcm():
    code_pd = linecache.getline("register.ini", 1).strip('\n')
    print("验证口令：" + code_pd)
    code_jm2 = "软件开发来自微信公众号：MD野生科技"
    if code_pd != code_jm2:
        # 创建主窗口
        root = tkinter.Tk()
        root.withdraw()

        curwidth = root.winfo_width()
        curhight = root.winfo_height()
        scn_w, scn_h = root.maxsize()
        cen_x = (scn_w - curwidth) / 2
        cen_y = (scn_h - curhight) / 2
        size_xy = '%dx%d+%d+%d' % (curwidth, curhight, cen_x, cen_y)
        root.geometry(size_xy)
        root.update()  # 窗体居中

        result1 = tkinter.simpledialog.askstring(title=version, prompt='获取此软件更新请关注微信公众号：MD野生科技\n\n'
                                                                       '请输入验证口令：', initialvalue='关注微信公众号可永久获得注册码')
        result = str(result1)

        if result != code_jm2:
            messagebox.showinfo("验证口令错误", "关注微信公众号：MD野生科技\n\n便可永久获得注册码")
            root.destroy()
            quit()

        if result == code_jm2:
            out_file = open("register.ini", 'w+', encoding='utf-8')
            out_file.write(result)
            out_file.close()
            root.destroy()
        # # 加入消息循环
        # root.mainloop()


if __name__ == '__main__':
    remove_line = [4, 7, 10, 13, 16, 19, 22, 25, 28]
    version = "InfobarTool_v1.0.0"
    b = win32gui.GetWindowRect(
        win32gui.FindWindowEx(
            win32gui.FindWindow("Shell_TrayWnd", None), 0, "ReBarWindow32", None))
    runtime = 0  # 程序运行起始时间

    # 注册码验证
    zcm()
    # os.system(r"taskkill /f /t /im " + version + ".exe")  # 通过cmd命令杀死前一个进程

    try:
        shiftx = int(linecache.getline("%s.ini" % version, remove_line[0]).replace(" ", "").strip('\n'))  # 去掉空格，去换行符
        bg_color = linecache.getline("%s.ini" % version, remove_line[1]).replace(" ", "").strip('\n')
        word_color = linecache.getline("%s.ini" % version, remove_line[2]).replace(" ", "").strip('\n')
        bgpd = int(linecache.getline("%s.ini" % version, remove_line[3]).replace(" ", "").strip('\n'))
        netpd = int(linecache.getline("%s.ini" % version, remove_line[4]).replace(" ", "").strip('\n'))
        select_pd = int(linecache.getline("%s.ini" % version, remove_line[5]).replace(" ", "").strip('\n'))
        d1_ckkd = int(linecache.getline("%s.ini" % version, remove_line[6]).replace(" ", "").strip('\n'))
        d1_ssjg = int(linecache.getline("%s.ini" % version, remove_line[7]).replace(" ", "").strip('\n'))
        d1_24hfz = int(linecache.getline("%s.ini" % version, remove_line[8]).replace(" ", "").strip('\n'))
        shiftx_new = shiftx

    except Exception as err:
        print(err)
        restore_w()
        shiftx = int(linecache.getline("%s.ini" % version, remove_line[0]).replace(" ", "").strip('\n'))  # 去掉空格，去换行符
        bg_color = linecache.getline("%s.ini" % version, remove_line[1]).replace(" ", "").strip('\n')
        word_color = linecache.getline("%s.ini" % version, remove_line[2]).replace(" ", "").strip('\n')
        bgpd = int(linecache.getline("%s.ini" % version, remove_line[3]).replace(" ", "").strip('\n'))
        netpd = int(linecache.getline("%s.ini" % version, remove_line[4]).replace(" ", "").strip('\n'))
        select_pd = int(linecache.getline("%s.ini" % version, remove_line[5]).replace(" ", "").strip('\n'))
        d1_ckkd = int(linecache.getline("%s.ini" % version, remove_line[6]).replace(" ", "").strip('\n'))
        d1_ssjg = int(linecache.getline("%s.ini" % version, remove_line[7]).replace(" ", "").strip('\n'))
        d1_24hfz = int(linecache.getline("%s.ini" % version, remove_line[8]).replace(" ", "").strip('\n'))
        shiftx_new = shiftx

    app = InfobarTool()
    app.mainloop()
