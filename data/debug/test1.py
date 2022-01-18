import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 创建函数
def askheight():
  # 获取浮点型数据（标题，提示，初始值）
  result = tkinter.simpledialog.askfloat(title = "获取信息",prompt="请输入身高（单位：米）：",initialvalue = "18.0")
  # 打印内容
  print(result)
# 添加按钮
btn = tkinter.Button(root,text = "获取身高",command = askheight)
btn.pack()

# 加入消息循环
root.mainloop()
