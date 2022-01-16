from PyQt5 import QtWidgets
from PyQt5.QtGui import QCursor
import win32gui
import psutil
import qtawesome
import sys
import time
from PyQt5.QtWidgets import QApplication, QMenu, QAction, qApp, QMessageBox
from Old.window import Ui_MainWindow
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class taskTool(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(taskTool, self).__init__()
        self.setupUi(self)
        self.widthx = 150
        self.shiftx = 40
        # 获取任务栏实例并重置任务栏大小
        m_hTaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
        m_hBar = win32gui.FindWindowEx(m_hTaskbar, 0, "ReBarWindow32", None)
        m_hMin = win32gui.FindWindowEx(m_hBar, 0, "MSTaskSwWClass", None)
        b = win32gui.GetWindowRect(m_hBar)
        win32gui.MoveWindow(m_hMin, 0, 0, b[2] - b[0] - self.widthx - self.shiftx, b[3] - b[1], True)  # 将MSTaskSwWClass缩小，预留窗口位置
        a = win32gui.GetWindowRect(m_hMin)
        # win32gui.MoveWindow(m_hMin, 0, 0, b[2] - b[0], b[3] - b[1], True)  # 程序退出请执行此句，调整任务栏为原始大小
        win32gui.SetParent(int(self.winId()), m_hBar)  # 设置任务栏为此窗口的父窗口
        # self.setGeometry(a[2] - a[0], 0, self.widthx, b[3] - b[1])
        self.setGeometry(b[2] - b[0] - self.widthx - self.shiftx, 0, self.widthx, b[3] - b[1])
        # 适配小任务栏
        if self.height() < 40:
            self.widget_cpu.hide()
            self.widget_mem.hide()
        else:
            self.widget_cpu.show()
            self.widget_mem.show()
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 置顶
        self.setWindowFlag(Qt.FramelessWindowHint)  # 无边框
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 透明背景
        self.iconOnButton()
        self.mainThread()
        # self.pushButton_mem.clicked.connect(self.rightMenuShow)
        # self.pushButton_cpu.clicked.connect(self.rightMenuShow)
        # self.pushButton_up.clicked.connect(self.rightMenuShow)
        # self.pushButton_down.clicked.connect(self.rightMenuShow)
        self.pushButton_mem.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_mem.customContextMenuRequested.connect(self.rightMenuShow)
        self.pushButton_cpu.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_cpu.customContextMenuRequested.connect(self.rightMenuShow)
        self.pushButton_up.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_up.customContextMenuRequested.connect(self.rightMenuShow)
        self.pushButton_down.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_down.customContextMenuRequested.connect(self.rightMenuShow)

    def iconOnButton(self):
        self.pushButton_cpu.setIcon(qtawesome.icon('fa.microchip', color='white'))
        self.pushButton_up.setIcon(qtawesome.icon('fa.long-arrow-up', color='white'))
        self.pushButton_down.setIcon(qtawesome.icon('fa.long-arrow-down', color='white'))
        self.pushButton_mem.setIcon(qtawesome.icon('fa.meetup', color='white'))

    def rightMenuShow(self, pos):  # 添加右键菜单
        menu = QMenu(self)
        menu.setStyleSheet("""\
                     QMenu {\
                     background-color:rgb(89,87,87); /*整个背景*/\
                     }\
                 QMenu::item {\
                     font-size: 10pt; \
                     color: rgb(225,225,225);  /*字体颜色*/\
                     background-color:rgb(89,87,87);\
                     padding:8px 10px; /*设置菜单项文字上下和左右的内边距，效果就是菜单中的条目左右上下有了间隔*/\
                     margin:2px 2px;/*设置菜单项的外边距*/\
                      }\
                 QMenu::item:selected { \
                     background-color:rgba(255,255,255,0.3);/*选中的样式*/\
                     }\
                 QMenu::item:pressed {/*菜单项按下效果*/\
                                           border: 1px solid rgb(60,60,61); \
                                           background-color: rgba(89,87,87, 0.5); \
                                       }\
                    """)
        quitAction = QAction("退出", self)
        quitAction.triggered.connect(self.appClose)
        self.hsnet = QAction("隐藏/显示网速", self)
        self.hsnet.triggered.connect(self.hsNetAction)
        self.hssys = QAction("隐藏/显示CPU、内存", self)
        self.hssys.triggered.connect(self.hsSysAction)
        menu.addAction(self.hsnet)
        menu.addAction(self.hssys)
        menu.addAction(quitAction)
        menu.exec_(QCursor.pos())

    def hsNetAction(self):
        if self.widget_up.isHidden():
            self.widget_down.show()
            self.widget_up.show()
        elif self.widget_cpu.isVisible():
            self.widget_down.hide()
            self.widget_up.hide()
        else:
            QMessageBox.information(self, '提示', '不能将信息全部隐藏')

    def hsSysAction(self):
        if self.widget_mem.isHidden():
            self.widget_mem.show()
            self.widget_cpu.show()
        elif self.widget_up.isVisible():
            self.widget_mem.hide()
            self.widget_cpu.hide()
        else:
            QMessageBox.information(self, '提示', '不能将信息全部隐藏')

    def mainThread(self):
        try:
            self.main_thread = Main_Thread()
            self.main_thread.thread_signal.connect(self.Update_UI)
            self.main_thread.start()
        except Exception as e:
            print(e)

    def Update_UI(self, msm):
        # import random
        self.pushButton_mem.setText(f"{msm['mem']}")
        self.pushButton_down.setText(f"{msm['down']}")
        self.pushButton_up.setText(f"{msm['up']}")
        self.pushButton_cpu.setText(f"{msm['cpu']}")
        # self.setToolTip("qqq")

    def appClose(self):
        # 将任务栏调整回原来大小
        m_hTaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
        m_hBar = win32gui.FindWindowEx(m_hTaskbar, 0, "ReBarWindow32", None)
        m_hMin = win32gui.FindWindowEx(m_hBar, 0, "MSTaskSwWClass", None)
        b = win32gui.GetWindowRect(m_hBar)
        win32gui.MoveWindow(m_hMin, 0, 0, b[2] - b[0], b[3] - b[1], True)
        a = win32gui.GetWindowRect(m_hMin)
        qApp.quit()


class Main_Thread(QThread):
    thread_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.info = {
            "cpu": "",
            "mem": "",
            "up": "",
            "down": ""
        }

    def run(self):
        def formatNum(size):
            ds = ['', 'K', 'M', 'G', 'T']
            for d in ds:
                if size < 1000:
                    if d:
                        return str(size) + d + "/s"
                    else:
                        return f'{round(size/1024, 1)}K/s'
                size = round(size / 1024, 1)
            return '0b/s'
        while True:
            self.info['cpu'] = f"{psutil.cpu_percent()}%"
            self.info['mem'] = f"{psutil.virtual_memory().percent}%"
            net0 = psutil.net_io_counters()
            time.sleep(1)
            net1 = psutil.net_io_counters()
            self.info['up'] = f"{formatNum((net1.bytes_sent - net0.bytes_sent) * 1)}"
            self.info['down'] = f"{formatNum((net1.bytes_recv - net0.bytes_recv) * 1)}"
            self.thread_signal.emit(self.info)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ex = taskTool()
    ex.show()
    sys.exit(app.exec_())