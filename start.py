import time
import logic.main as main
import utility.device as device
import utility.user32 as user32
import utility.log as log
import utility.xml as xml

full_path = r'E:\GitHub\AutoTest\AutoTest\bin\Debug\AutoTest.exe'

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

    # 打开设备
    if not device.open_device(): exit

    # 初期化
    users = xml.get_users_value()

    # 处理开始
    for key in users.keys():
        log.log_info(f'User Start:{key}')
        for value,name,cnt,envent in users[key]:
            log.log_info(f'User Role:{value} {name}')
            #
            main.start(key,value,name,cnt,envent)
            #
            xml.set_step_value(time.strftime("%Y%m%d", time.localtime()),key,cnt)

    # 关闭设备
    device.close_device()

    log.log_info('----- Script  End  -----')
