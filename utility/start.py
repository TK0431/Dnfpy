import os
import time
import utility.user32 as user32
import utility.log as log
import win32.win32api as wapi

def exe_start(name, full_path, cnts = 3):
    '''
    启动应用程序
    '''
    hwnd = 0
    # 启动前信息确认
    if not exe_check(name, full_path): return hwnd

    cnt = 1 # 启动次数
    while hwnd == 0 and cnt <= cnts:
        log.log_info('第{cnt}次尝试启动…'.format_map(vars()))
        # 启动应用程序
        hwnd = start_try(name, full_path)
        if hwnd:
            log.log_info('第{cnt}次尝试启动成功({hwnd})!'.format_map(vars()))
        else:
            log.log_warn('第{cnt}次尝试启动失败!'.format_map(vars()))
        cnt += 1

    # 启动成功判断
    if not hwnd:
        log.log_error('应用程序{full_path}启动失败!'.format_map(vars()))

    return hwnd

def exe_check(name, full_path):
    '''
    启动前信息确认
    '''
    # 应用程序名确认
    if name == '' or name == None:
        log.log_error('Exe Name Empty')
        return False

    # Exe启动路径确认
    if not os.path.exists(full_path):
        log.log_error('Exe path not right {full_path}'.format_map(vars()))
        return False

    return True

def start_try(name, full_path, sleep_time = 3):
    '''
    启动应用程序
    '''
    os.startfile(full_path)
    # wapi.ShellExecute(0, 'open', full_path, '','',1)
    # os.system('start {full_path}'.format_map(vars()))

    time.sleep(sleep_time)

    if name == '':
        start_dnf()

    return user32.get_hwnd(name)

def start_dnf(full_path):
    pass
