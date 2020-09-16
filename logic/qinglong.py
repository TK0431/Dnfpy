import win32api
import time

def skill1(hwnd):
    time.sleep(3)
    win32api.keybd_event(65,0x1e,0,0)
    time.sleep(1)
    win32api.keybd_event(65,0x1e,0,0)
    time.sleep(1)
    win32api.keybd_event(65,0x1e,0,0)
    time.sleep(1)
    win32api.keybd_event(65,0x1e,0,0)
    time.sleep(1)

import ctypes as C

def skill2():
    msdk = C.CDLL(r'E:\GitHub\Dnfpy\logic\sxAnswer.dll',C.RTLD_GLOBAL)
    if msdk.OpenDevice()==1:
        print("打开设备成功！")
    else:
        print("打开设备失败！")

skill2()