import utility.user32 as user32
import utility.log as log
import utility.device as device
import ctypes as C
import time

def start(key,value,name,cnt):
    while True:
        # 获取Hwnd
        hwnd = user32.get_hwnd(name)
        if hwnd == 0:
            # 重启Exe
            # hwnd = start.exe_start(name, full_path)
            # 
            # 重启失败，结束脚本
            if hwnd == 0:
                break

        # 获取置顶窗口
        top_hwnd = user32.get_top_hwnd()
        if top_hwnd == hwnd:
            do_event(hwnd)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)

def do_event():
    device.key_press(b'space')
    time.sleep(3)
    device.key_press(b'down',cnt = 2)
    device.key_press(b'space')
    time.sleep(3)
    device.key_press(b'num1')
    device.key_press(b'enter',2)
    time.sleep(1)
    device.key_press(b'x', cnt=3)
