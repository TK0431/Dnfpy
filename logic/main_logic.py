import utility.device as device
import utility.user32 as user32

def main_start(hwnd):
    while True:
        for 

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
            logic.main_start(hwnd)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)

        xml.set_step_value(time.strftime("%Y%m%d", time.localtime()),user,cnt)

    device.open_device()
    device.key_press(b'a')
    device.key_press(b'space')
    device.key_press(b'down',cnt = 2)
    device.key_press(b'space')
    device.key_press(b'num1')
    device.key_press(b'enter')
    device.key_press(b'x', cnt=3)

