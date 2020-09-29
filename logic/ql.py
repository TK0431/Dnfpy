import utility.user32 as user32
import utility.log as log
import utility.device as device
import utility.xml as xml
import ctypes as C
import time
import random 

from enum import Enum


class ql_type(Enum):
    unknow = 0
    progress = 1
    order = 2
    open = 3
    start = 4
    ready1 = 5
    ready2 = 6
    fite = 7
    skilled = 8
    win = 9
    wined = 10
    goods = 11
    end = 12
    next = 13
    sell = 14
    quite = 15
    out = 16

over_cnt = 0

def start(key, value, name, cnt):
    points = xml.get_points_value('ql')
    state = ql_type.unknow
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
            old = do_event(hwnd, points, state)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)


def do_event(hwnd, points, state):
    if state == ql_type.unknow:
        return do_unknow(hwnd, points)
    elif state == ql_type.progress:
        return do_progress(points)
    elif state == ql_type.order:
        return do_order(points)
    elif start == ql_type.open:
        return do_open(points)
    elif start == ql_type.start:
        return do_start(points)
    elif start == ql_type.fite:
        return do_fite(points)
    elif start == ql_type.skilled:
        return do_skilled(points)

def do_progress(points,cnt = 0):
    '''
    进度条读取
    '''
    if point_judge(points, 'ql_progress'):
        log.log_info("进度：读取中...")
        return ql_type.progress
    elif point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("进度：进入排表，已按下Space...")
        return ql_type.order
    elif cnt >= 10:
        log.log_info("进度：未知...")
        # 保存图片
        return ql_type.unknow
    else:
        # get new pic
        log.log_info("进度：未知{cnt}尝试...")
        return do_progress(points,cnt+1)

def do_order(points, cnt = 0):
    '''
    排表
    '''
    if point_judge(points, 'ql_open'):
        # device.key_press(b'space')
        log.log_info('排表：大门打开,已按下Space...')
        return ql_type.open
    elif point_judge(points, 'ql_order'):
        log.log_info("排表：等待进入大门...")
        return ql_type.order
    elif point_judge(points, 'ql_progress'):
        log.log_info("排表：等待进入排表...")
        return ql_type.order
    elif cnt >= 10:
        log.log_info("排表：未知...")
        # 保存图片
        return ql_type.unknow
    else:
        # get new pic
        log.log_info("排表：未知{cnt}尝试...")
        return do_order(points,cnt+1)

def do_open(points, cnt = 0):
    '''
    大门
    '''
    if point_judge(points, 'ql_start'):
        log.log_info('大门：进入开始...')
        return ql_type.start
    elif point_judge(points, 'ql_open'):
        log.log_info("大门：等待进入开始...")
        return ql_type.open
    elif point_judge(points, 'ql_order'):
        log.log_info("大门：等待进入大门...")
        return ql_type.open
    elif cnt >= 10:
        log.log_info("大门：未知...")
        # 保存图片
        return ql_type.unknow
    else:
        # get new pic
        log.log_info("大门：未知{cnt}尝试...")
        return do_open(points,cnt+1)

def do_start(points, cnt = 0):
    '''
    开始
    '''
    if point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        # device.key_press(b'space')
        log.log_info("开始：准备，已按下Space...")
        return ql_type.ready
    elif cnt >= 30:
        log.log_info("开始：未知...")
        # 保存图片
        return ql_type.unknow
    else:
        # get new pic
        time.sleep(0.1)
        log.log_info("开始：未知{cnt}尝试...")
        return do_start(points, cnt + 1)

def do_ready(points):
    '''
    准备
    '''
    if point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        log.log_info("准备：等待fite...")
        return ql_type.ready
    else:
        # device.key_press(b'q')
        log.log_info("准备：Q已按下...")
        time.sleep(0.5)
        return ql_type.fite

def do_fite(points):
    '''
    Fite
    '''
    if point_judge(points, 'ql_win'):
        # device.key_press(b'space')
        log.log_info("Fite：Win，已按下Space...")
        return ql_type.win
    elif point_judge(points, 'ql_skilled'):
        log.log_info("Fite：Skilled...")
        return ql_type.skilled
    else:
        # device.key_press(b'q')
        log.log_info("Fite：Q已按下...")
        time.sleep(0.5)
        return ql_type.fite

def do_skilled(points,cnt = 0):
    '''
    Skilled
    '''
    if point_judge(points, 'ql_win'):
        # device.key_press(b'space')
        log.log_info("Skilled：Win，已按下Space...")
        return ql_type.win

    if None and point_judge(points, 'ql_w'):
        log.log_info("Skilled：W已按下...")

    if cnt > 60:
        log.log_info("Skilled：超时...")
        # 保存图片
        return ql_type.unknow
    else:
        log.log_info("Skilled：等待{cnt}尝试...")
        time.sleep(0.5)
        return ql_type.skilled

def do_win(points, cnt = 0):
    if point_judge(points, 'ql_win'):
        log.log_info("Win：等待Win结束...")
        return ql_type.win
    elif point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("Win：已按下Space...")
        return ql_type.order
    elif judeg_goods(points):
        # device.key_press(b'num1')
        # device.key_press(b'x')
        log.log_info("Win：Get Good...")
        return ql_type.goods
    elif cnt > 9:
        log.log_info("Win：超时...")
        # 保存图片
        return ql_type.unknow
    else:
        log.log_info("Win：等待{cnt}尝试...")
        time.sleep(0.5)
        return ql_type.win

def do_goods(points):
    '''
    商品
    '''
    if judeg_goods(points):
        # device.key_press(b'x')
        log.log_info("Goods：Get Good...")
        return ql_type.goods
    elif point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("Goods：已按下Space...")
        return ql_type.order
    elif point_judge(points, 'ql_end'):
        log.log_info("Goods：进去End...")
        return ql_type.wined

def do_wined(points, cnt = 0):
    '''
    结算
    '''
    global over_cnt
    if point_judge(points, 'ql_end'):
        time.sleep(0.5)
        log.log_info("Wined：等待...")
        return ql_type.wined
    elif point_judge(points, 'ql_next'):
        if over_cnt >= 10 and random.randint(0,4) == 0:
            over_cnt = 0
            # device.key_press(b'f12')
            log.log_info("Wined：已退出...")
            return ql_type.quite
        else:
            over_cnt += 1
            # device.key_press(b'space')
            log.log_info("Wined：已按下Space...")
            return ql_type.next
    elif cnt > 9:
        log.log_info("Wined：未知...")
        # 保存图片
        return ql_type.unknow
    else:
        log.log_info("Wined：未知{cnt}尝试...")
        time.sleep(0.5)
        return ql_type.wined

def do_next(points):
    '''
    再次
    '''
    if point_judge(points, 'ql_progress'):
        log.log_info("Next：进度...")
        return ql_type.progress
    elif point_judge(points, 'ql_next'):
        log.log_info("Next：等待...")
        return ql_type.next

def do_quite(points):
    '''
    退出
    '''
    if point_judge(points, 'ql_out'):
        device.mouse_move(100,100)
        device.mouse_left_click()
        log.log_info("Out：Start Sell...")
        return ql_type.sell
    elif point_judge(points, 'ql_next'):
        log.log_info("Next：等待...")
        return ql_type.next
    for i in range(1,10):
        pass


def do_sell(points):
    '''
    Sells
    '''
    

def do_unknow(hwnd, points):
    '''
    未知
    '''
    if point_judge(points, 'ql_dzb'):
        device.key_press(b'space')
        return
    if point_judge(points, 'ql_zb_1'):
        device.key_press(b'space')
        return
    if point_judge(points, 'ql_zb_2'):
        device.key_press(b'space')
        return
    if point_judge(points, 'ql_f10'):
        device.key_press(b'f10')
        return
    if point_judge(points, 'ql_over'):
        device.key_press(b'space')
        # .....
        return
    if point_judge(points, 'ql_qr'):
        device.key_press(b'space')
        return
    if point_judge(points, 'ql_door'):
        time.sleep(0.1)
        return
    if point_judge(points, 'ql_skill'):
        device.key_press(b'right', cnt=2)
        device.key_press(b'space')
        return


def judeg_goods(points):
    return False

def point_judge(points, value, cnt):
    x, y, r, g, b = points[value][cnt]
    rr, gg, bb = user32.get_win_rgb(x, y)
    if r == rr and g == gg and b == bb:
        if cnt == 2:
            return True
        else:
            return point_judge(points, value, cnt + 1)
    else:
        return False
