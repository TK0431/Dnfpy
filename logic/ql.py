import utility.user32 as user32
import utility.log as log
import utility.device as device
import utility.xml as xml
import ctypes as C
import time
import random
import cv2
import shutil
from enum import Enum
from functools import wraps
from datetime import datetime


class ql_type(Enum):
    unknow = 0   # 未知
    progress = 1  # 进度条
    order = 2    # 对战表
    door = 3     # 大门
    start = 4    # 开始
    ready = 5   # 准备1
    fite = 7     # 对战
    win = 9      # 获胜
    goods = 10   # 捡物品
    end = 12     # 结算
    next = 13    # 继续
    out = 14     # 退出
    map = 15     # 地图
    sell = 16    # 售卖
    over = 17    # 结束


hwnd = None
over_cnt = 0
old_state = ql_type.unknow


def start(key, value, name, cnt):
    """
    青龙循环入口
    """
    global hwnd
    points = xml.get_points_value('ql')
    state = ql_type.unknow
    while True:
        time.sleep(0.1)
        # 获取Hwnd
        hwnd = user32.get_hwnd('地下城与勇士')
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
            state = do_event(hwnd, points, state)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)


def do_event(hwnd, points, state):
    '''
    循环事件
    '''
    global img
    img = get_img()

    if state == ql_type.unknow:
        return do_unknow(img, points)
    elif state == ql_type.progress:
        return do_progress(img, points)
    elif state == ql_type.order:
        return do_order(img, points)
    elif state == ql_type.door:
        return do_door(img, points)
    elif state == ql_type.start:
        return do_start(img, points)
    elif state == ql_type.ready:
        return do_ready(img, points)
    elif state == ql_type.fite:
        return do_fite(img, points, 0, 300)
    elif state == ql_type.win:
        return do_win(img, points)
    elif state == ql_type.win:
        return do_wined(img, points)
    elif state == ql_type.goods:
        return do_goods(img, points)
    elif state == ql_type.end:
        return do_end(img, points)
    elif state == ql_type.next:
        return do_next(img, points)
    elif state == ql_type.out:
        return do_out(img, points,0,300)
    elif state == ql_type.map:
        return do_map(img, points)
    elif state == ql_type.sell:
        return do_sell(img, points)
    elif state == ql_type.over:
        return do_over(img, points)
    else:
        return ql_type.unknow


def loop_unknow(func):
    '''
    未知Loop
    '''
    def loop_function(*args, **kwargs):
        cnt = 0 if len(args) == 2 else args[2]
        times = 100 if len(args) < 4 else args[3]
        result = func(*args, **kwargs)
        if result == ql_type.unknow:
            if cnt > times:
                log.log_warn('Loop:未知...')
                copy_img()
                return ql_type.unknow
            else:
                time.sleep(0.1)
                img = get_img()
                return loop_function(img, args[1], cnt+1, times)
        else:
            return result
    return loop_function


@loop_unknow
def do_out(img, points, cnt=0, times=100):
    '''
    售卖
    '''
    if point_judge(img, points, 'ql_map') or point_judge(img, points, 'ql_map1'):
        return do_log(ql_type.map, "售卖->地图：选择地图中...")
    elif point_judge(img, points, 'ql_out'):
        # ********************
        #
        return do_log(ql_type.out, "售卖：地图外等待...")
    else:
        return ql_type.unknow


@loop_unknow
def do_map(img, points, cnt=0, times=100):
    '''
    地图
    '''
    if point_judge(img, points, 'ql_map'):
        device.key_press(b'space')
        return do_log(ql_type.progress, "地图：目标地图，已按下Space...")
    elif point_judge(img, points, 'ql_map1'):
        device.key_press(b'up')
        return do_log(ql_type.map, "地图：非目标地图，已按下Up...")
    else:
        return ql_type.unknow


@loop_unknow
def do_progress(img, points, cnt=0, times=100):
    '''
    进度条读取
    '''
    if point_judge(img, points, 'ql_order'):
        device.key_press(b'space')
        return do_log(ql_type.order, "进度->对战表:已按下Space...")
    elif point_judge(img, points, 'ql_progress'):
        # 进度：读取中...
        return ql_type.progress
    else:
        return ql_type.unknow


@loop_unknow
def do_order(img, points, cnt=0, times=100):
    '''
    对战表
    '''
    if point_judge(img, points, 'ql_door'):
        device.key_press(b'space')
        return do_log(ql_type.door, '对战表：已进入大门,已按下Space...')
    elif point_judge(img, points, 'ql_order'):
        # "对战表：等待进入大门..."
        return ql_type.order
    else:
        return ql_type.unknow


@loop_unknow
def do_door(img, points, cnt=0, times=100):
    '''
    大门
    '''
    if point_judge(img, points, 'ql_start'):
        return do_log(ql_type.start, '大门：已经开始...')
    elif point_judge(img, points, 'ql_door'):
        # "大门：等待进入开始..."
        return ql_type.door
    else:
        return ql_type.unknow


@loop_unknow
def do_start(img, points, cnt=0, times=100):
    '''
    开始
    '''
    if point_judge(img, points, 'ql_ready1') or point_judge(img, points, 'ql_ready2'):
        device.key_press(b'space')
        return do_log(ql_type.ready, "开始：进入准备，已按下Space...")
    elif point_judge(img, points, 'ql_start'):
        return do_log(ql_type.start, '开始：等待进入准备...')
    else:
        return ql_type.unknow


@loop_unknow
def do_ready(img, points, cnt=0, times=100):
    '''
    准备
    '''
    if point_judge(img, points, 'ql_fite'):
        device.key_press(b'q')
        return do_log(ql_type.fite, "准备：Skill Q已按下...")
    elif point_judge(img, points, 'ql_ready1') or point_judge(img, points, 'ql_ready2'):
        return do_log(ql_type.ready, "准备：等待进入对战...")
    else:
        return ql_type.unknow


@loop_unknow
def do_fite(img, points, cnt=0, times=100):
    '''
    对战
    '''
    if point_judge(img, points, 'ql_win'):
        device.key_press(b'space')
        return do_log(ql_type.win, "对战：获胜，已按下Space...")
    elif point_judge(img, points, 'ql_fite'):
        return do_log(ql_type.fite, "对战：对战中...")
    else:
        return ql_type.unknow


@loop_unknow
def do_win(img, points, cnt=0, times=100):
    '''
    获胜
    '''
    if point_judge(img, points, 'ql_order'):
        device.key_press(b'space')
        return do_log(ql_type.order, "获胜：进入对战表,已按下Space...")
    elif point_judge(img, points, 'ql_ready1') or point_judge(img, points, 'ql_ready2'):
        device.key_press(b'space')
        return do_log(ql_type.ready, "获胜：进入准备，已按下Space...")
    elif judeg_goods(img):
        device.key_press(b'num1')
        device.key_press(b'x')
        return do_log(ql_type.goods, "获胜：num1 和 x拾取物品...")
    elif point_judge(img, points, 'ql_end'):
        return do_log(ql_type.end, "获胜：进入结算...")
    else:
        return ql_type.unknow


@loop_unknow
def do_goods(img, points, cnt=0, times=100):
    '''
    捡物品
    '''
    if point_judge(img, points, 'ql_order'):
        device.key_press(b'space')
        return do_log(ql_type.order, "捡物品：进入对战表,已按下Space...")
    elif point_judge(img, points, 'ql_ready1') or point_judge(img, points, 'ql_ready2'):
        device.key_press(b'space')
        return do_log(ql_type.ready, "捡物品：进入准备，已按下Space...")
    elif point_judge(img, points, 'ql_end'):
        return do_log(ql_type.end, "捡物品：进入结算...")
    elif cnt == 0 and judeg_goods(img):
        device.key_press(b'x')
        return do_log(ql_type.goods, "捡物品：拾取物品...")
    else:
        return ql_type.unknow


@loop_unknow
def do_end(img, points, cnt=0, times=100):
    '''
    结算
    '''
    if point_judge(img, points, 'ql_next'):
        return do_log(ql_type.next, "结算：是否再次...")
    elif point_judge(img, points, 'ql_end'):
        return do_log(ql_type.end, "结算：结算中...")
    else:
        return ql_type.unknow


@loop_unknow
def do_next(img, points, cnt=0, times=100):
    '''
    继续
    '''
    global over_cnt
    if judeg_goods(img):
        device.key_press(b'x')
        return do_log(ql_type.next, "继续：拾取物品...")
    if point_judge(img, points, 'ql_next'):
        if over_cnt >= 10 and random.randint(0, 4) == 0:
            over_cnt = 0
            device.key_press(b'f12')
            return do_log(ql_type.out, "继续：已退出...")
        else:
            over_cnt += 1
            device.key_press(b'f10')
            return do_log(ql_type.progress, "继续：已按下F10...")
    else:
        return ql_type.unknow

@loop_unknow
def do_over(img, points, cnt=0, times=100):
    '''
    终了
    '''
    device.key_press(b'f12')
    return do_log(ql_type.progress, "终了：已按下F12...")


def do_unknow(img, points):
    '''
    未知
    '''
    if point_judge(img, points, 'ql_out'):
        return ql_type.out
    elif point_judge(img, points, 'ql_progress'):
        return ql_type.progress
    elif point_judge(img, points, 'ql_map'):
        return ql_type.map
    elif point_judge(img, points, 'ql_map1'):
        return ql_type.map
    elif point_judge(img, points, 'ql_order'):
        return ql_type.order
    elif point_judge(img, points, 'ql_door'):
        return ql_type.door
    elif point_judge(img, points, 'ql_win'):
        return ql_type.win
    elif point_judge(img, points, 'ql_end'):
        return ql_type.end
    elif point_judge(img, points, 'ql_next'):
        return ql_type.next
    elif point_judge(img, points, 'ql_ready1'):
        return ql_type.ready
    elif point_judge(img, points, 'ql_ready2'):
        return ql_type.ready
    elif point_judge(img, points, 'ql_start'):
        return ql_type.start
    elif point_judge(img, points, 'ql_fite'):
        return ql_type.fite
    else:
        return ql_type.unknow


def judeg_goods(img, x=560, y=330):
    '''
    判断是否有商品
    '''
    for y0 in range(26):
        for x0 in range(1280-x):
            
            y1 = y0*15
            bb = img[ y+y1, x+x0,0]
            gg = img[y+y1, x+x0, 1]
            rr = img[y+y1, x+x0, 2]
            if judge_goods_color(rr,gg,bb): return True
            bb = img[ y-y1, x+x0,0]
            gg = img[y-y1, x+x0, 1]
            rr = img[y-y1, x+x0, 2]
            if judge_goods_color(rr,gg,bb): return True
            if x - x0 > 0: 
                bb = img[ y+y1,x-x0, 0]
                gg = img[y+y1,x-x0, 1]
                rr = img[y+y1,x-x0, 2]
                if judge_goods_color(rr,gg,bb): return True
                bb = img[ y-y1,x-x0, 0]
                gg = img[y-y1,x-x0, 1]
                rr = img[y-y1,x-x0, 2]
                if judge_goods_color(rr,gg,bb): return True
    return False

def judge_goods_color(r,g,b):
    # 紫色物品
    if r == 179 and g == 107 and b == 255: return True
    # 黄色边框
    if r == 238 and g == 236 and b == 2: return True
    # 蓝色物品
    if r == 104 and g == 213 and b == 237: return True
    return False


def point_judge(img, points, value, cnt=0):
    '''
    类型判断
    '''
    x, y, r, g, b = points[value][cnt]
    xx = int(x)
    yy = int(y)
    bb = str(img[yy, xx, 0])
    gg = str(img[yy, xx, 1])
    rr = str(img[yy, xx, 2])
    if r == rr and g == gg and b == bb:
        if cnt == 2:
            return True
        else:
            return point_judge(img, points, value, cnt + 1)
    else:
        return False


def get_img():
    '''
    获取图片
    '''
    user32.get_pic(hwnd, 'dnf')
    return cv2.imread(r'img/dnf.png')


def copy_img():
    '''
    复制图片
    '''
    shutil.copy('img\\dnf.png', 'img\\' +
                datetime.now().strftime('%Y%m%d%H%M%S%f') + '.png')


def do_log(state, msg):
    '''
    日志
    '''
    global old_state
    if state != old_state:
        old_state = state
        log.log_info(msg)
    return state
