import time
import utility.start as start
import utility.user32 as user32
import utility.log as log
import logic.main_logic as logic

full_path = r'E:\GitHub\AutoTest\AutoTest\bin\Debug\AutoTest.exe'
name = 'MainWindow'
debug_flg = True
sleep_time = 0.1

if __name__ == "__main__":
    '''
    程序主启动窗口
    '''
    # 测试模式启动控制台Log
    if debug_flg:
        log.log_console_start()

    log.log_info('----- Script Start -----')

    # 处理开始
    while True:
        # 处理时间间隔
        time.sleep(sleep_time)

        # 获取Hwnd
        hwnd = user32.get_hwnd(name)
        if hwnd == 0:
            # 重启Exe
            hwnd = start.exe_start(name, full_path)
            # 
            if hwnd == 0:
                break
        else:
            logic.main_start(hwnd)

        break

    log.log_info('----- Script  End  -----')
