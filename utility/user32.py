import win32gui


def get_hwnd(name, cls=None):
    """
    获取窗口
    name:窗口名
    cls:窗口类
    """
    return win32gui.FindWindow(cls, name)

def get_top_hwnd():
    return win32gui.GetForegroundWindow()