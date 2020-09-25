import utility.user32 as user32
import utility.log as log
import utility.device as device
import utility.xml as xml
import ctypes as C
import time

def start(key,value,name,cnt):
    points = xml.get_points_value('ql')
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
            do_event(hwnd, points)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)

def do_event(hwnd, points):
    # dzb
    if point_judge(points,'ql_dzb') : 
        device.key_press(b'space')
        return
    if point_judge(points,'ql_zb_1'):
        device.key_press(b'space')
        return
    if point_judge(points,'ql_zb_2'):
        device.key_press(b'space')
        return
    if point_judge(points,'ql_f10'): 
        device.key_press(b'f10')
        return
    if point_judge(points,'ql_over'): 
        device.key_press(b'space')
        # .....
        return
    if point_judge(points,'ql_qr'): 
        device.key_press(b'space')
        return
    if point_judge(points,'ql_door'): 
        time.sleep(0.1)
        return
    if point_judge(points,'ql_skill'):
        device.key_press(b'right',cnt = 2)
        device.key_press(b'space')
        return

def point_judge(points, value, cnt):
    x,y,r,g,b = points[value][cnt]
    rr,gg,bb = user32.get_win_rgb(x,y)
    if r==rr and g==gg and b==bb:
        if cnt == 2:
            return True
        else:
            return point_judge(points, value, cnt + 1)
    else:
        return False

