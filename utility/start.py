import os
import utility.user32 as user32

def start_exe(name, full_path, cnts = 3):
    '''
    启动应用程序
    '''
    hwnd = 0
    cnt = 1
    while hwnd == 0 and cnt <= cnts:
        hwnd = try_start(name, full_path)
        if hwnd:
            print('第{cnt}次尝试启动成功({hwnd})!'.format_map(vars()))
        else:
            print('第{cnt}次尝试启动失败({hwnd})!'.format_map(vars()))
        cnt += 1

    if not hwnd:
        print('应用程序启动失败!')
    return hwnd

def try_start(name, full_path):
    os.startfile(full_path)
    return user32.get_hwnd(name)