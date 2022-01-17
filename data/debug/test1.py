import psutil
import os


def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print(pid)
            return True
        else:
            pass
    return False


# "tasklist|find /i "InfobarTool.exe""
ab = os.popen('''tasklist|find /i "InfobarTool.exe"''')
if ab.read() == None:
    print(11)
