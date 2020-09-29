import win32gui
import win32api
import win32con
import win32ui
import numpy as np
from ctypes import *


def get_hwnd(name, cls=None):
    """
    获取窗口
    name:窗口名
    cls:窗口类
    """
    return win32gui.FindWindow(cls, name)


def set_top_hwnd(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def get_top_hwnd():
    return win32gui.GetForegroundWindow()


def get_win_pos(hwnd):
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    return l, t, r-l, b-t


def get_mouse_pos():
    return win32api.GetCursorPos()

def get_win_rgbs(x, y, w = 20, h = 20):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    img = np.zeros((h, w, 3), dtype=np.uint8)
    for row in range(y, y+h):
        for col in range(x, x+w):
            pixel = gdi32.GetPixel(hdc, col, row)
            r = pixel & 0x0000ff
            g = (pixel & 0x00ff00) >> 8
            b = pixel >> 16
            img[row-y, col-x, 0] = b
            img[row-y, col-x, 1] = g
            img[row-y, col-x, 2] = r
    return img

# 0.02s
def get_win_rgb(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return r, g, b

from functools  import wraps
import time

def timefn(fn):
    @wraps(fn)
    def get_diff_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f'@timefn: {fn.__name__} took {t2 - t1: .5f} s')
        return result

    return get_diff_time

def get_pic(hwnd, fname = 'test'):
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    _,_,w,h=    get_win_pos(hwnd)
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    try:
        saveBitMap.SaveBitmapFile(saveDC, f'img\\{fname}.jpg')
    except Exception:
        pass
