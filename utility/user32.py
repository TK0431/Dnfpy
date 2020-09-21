import win32gui
import win32api
import win32con
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


def set_win_pos(hwnd):
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    return l, t, r-l, b-t

def get_mouse_pos():
    return win32api.GetCursorPos()

def print_mouse_pos():
    x,y = win32api.GetCursorPos()
    print(x,y)

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


def get_win_rgb(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return r, g, b
