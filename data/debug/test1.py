import win32gui

# 将MSTaskSwWClass缩小[数字分别表示该窗口的左侧/顶部/右侧/底部坐标]，预留窗口位置
m_htaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
m_hbar = win32gui.FindWindowEx(m_htaskbar, 0, "ReBarWindow32", None)
m_hmin = win32gui.FindWindowEx(m_hbar, 0, "MSTaskSwWClass", None)

bm_hmin = win32gui.GetWindowRect(m_hmin)
bm_hbar = win32gui.GetWindowRect(m_hbar)
bm_htaskbar = win32gui.GetWindowRect(m_htaskbar)
print(bm_htaskbar)
print(bm_hbar)
print(bm_hmin)


