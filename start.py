import time
import utility.start as start
import utility.user32 as user32
import utility.log as log
import logic.main_logic as logic

full_path = r'E:\GitHub\AutoTest\AutoTest\bin\Debug\AutoTest.exe'
name = 'AutoTest'
debug_flg = True
sleep_time = 0.1

if __name__ == "__main__":
    '''
    程序主启动窗口1

    '''
    # 测试模式启动控制台Log
    if debug_flg:
        log.log_console_start()

    log.log_info('----- Script Start -----')
    cnt = 0
    # 处理开始
    while True:
        # 处理时间间隔 
        # time.sleep(sleep_time)

        # 获取Hwnd
        hwnd = user32.get_hwnd(name)
        if hwnd == 0:
            # 重启Exe1
            # hwnd = start.exe_start(name, full_path)
            # 
            # 重启失败，结束脚本
            if hwnd == 0:
                break
        else:
            # user32.set_top_hwnd(hwnd)
            top_hwnd = user32.get_top_hwnd()
            if top_hwnd == hwnd:
                logic.main_start(hwnd)
            else:
                pass
            print(str(cnt))
            cnt+=1

    log.log_info('----- Script  End  -----')
