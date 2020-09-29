import utility.user32 as user32
import utility.log as log
import utility.device as device
import utility.xml as xml
import ctypes as C
import time
import random
import shutil
from enum import Enum


class ql_type(Enum):
    unknow = 0   # 未知
    progress = 1  # 进度条
    order = 2    # 对战表
    open = 3     # 大门
    start = 4    # 开始
    ready1 = 5   # 准备1
    ready2 = 6   # 准备2
    fite = 7     # 对战
    win = 9      # 获胜
    goods = 10   # 捡物品
    end = 12     # 结算
    next = 13    # 继续
    out = 14     # 退出
    sell = 14    # 售卖


def start(key, value, name, cnt):
    points = xml.get_points_value('ql')
    start = ql_type.unknow
    while True:
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
            state = do_event(hwnd, points, start)
        else:
            # 等待后继续尝试
            log.log_info('窗口未置顶，等待...')
            time.sleep(5)


def do_event(hwnd, points, state):
    '''
    循环事件
    '''
    img = get_img()

    if state == ql_type.unknow:
        return do_unknow(img, points)
    elif state == ql_type.progress:
        return do_progress(img, points)
    elif state == ql_type.order:
        return do_order(img, points)
    elif start == ql_type.open:
        return do_open(img, points)
    elif start == ql_type.start:
        return do_start(img, points)
    elif start == ql_type.ready1 or start == ql_type.ready2:
        return do_ready(img, points)
    elif start == ql_type.fite:
        return do_fite(img, points)
    elif start == ql_type.win:
        return do_win(img, points)
    elif start == ql_type.wined:
        return do_wined(img, points)
    elif start == ql_type.goods:
        return do_goods(img, points)
    elif start == ql_type.end:
        return do_end(img, points)
    elif start == ql_type.next:
        return do_next(img, points)
    elif start == ql_type.out:
        return do_out(img, points)
    elif start == ql_type.sell:
        return do_sell(img, points)


def do_progress(img, points, cnt=0):
    '''
    进度条读取
    '''
    if point_judge(points, 'ql_progress'):
        log.log_info("进度：读取中...")
        return ql_type.progress
    elif point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("进度：已进入对战表，已按下Space...")
        return ql_type.order
    elif cnt >= 10:
        log.log_info("进度：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("进度：未知{cnt}尝试...")
        return do_progress(img, points, cnt+1)


def do_order(img, points, cnt=0):
    '''
    对战表
    '''
    if point_judge(points, 'ql_open'):
        # device.key_press(b'space')
        log.log_info('对战表：已进入大门,已按下Space...')
        return ql_type.open
    elif point_judge(points, 'ql_order'):
        log.log_info("对战表：等待进入大门...")
        return ql_type.order
    elif cnt >= 10:
        log.log_info("对战表：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("对战表：未知{cnt}尝试...")
        return do_order(img, points, cnt+1)


def do_open(img, points, cnt=0):
    '''
    大门
    '''
    if point_judge(points, 'ql_start'):
        log.log_info('大门：已经开始...')
        return ql_type.start
    elif point_judge(points, 'ql_open'):
        log.log_info("大门：等待进入开始...")
        return ql_type.open
    elif cnt >= 10:
        log.log_info("大门：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("大门：未知{cnt}尝试...")
        return do_open(img, points, cnt+1)


def do_start(img, points, cnt=0):
    '''
    开始
    '''
    if point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        # device.key_press(b'space')
        log.log_info("开始：进入准备，已按下Space...")
        return ql_type.ready
    elif cnt >= 10:
        log.log_info("开始：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("开始：未知{cnt}尝试...")
        return do_start(img, points, cnt + 1)


def do_ready(img, points,cnt = 0):
    '''
    准备
    '''
    if point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        log.log_info("准备：等待对战...")
        return ql_type.ready
    else:
        # device.key_press(b'q')
        log.log_info("准备：Skill Q已按下...")
        time.sleep(0.5)
        return ql_type.fite


def do_fite(img, points, cnt = 0):
    '''
    对战
    '''
    if point_judge(points, 'ql_win'):
        # device.key_press(b'space')
        log.log_info("对战：获胜，已按下Space...")
        return ql_type.win
    elif cnt > 100:
        log.log_info("对战：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("对战：对战中...")
        return do_fite(img, points, cnt+1)


def do_win(img, points, cnt=0):
    '''
    获胜
    '''
    if point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("获胜：进入对战表,已按下Space...")
        return ql_type.order
    elif point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        # device.key_press(b'space')
        log.log_info("获胜：进入准备，已按下Space...")
        return ql_type.ready
    elif point_judge(points, 'ql_end'):
        log.log_info("获胜：进入结算...")
        return ql_type.end
    elif judeg_goods(points):
        # device.key_press(b'num1')
        # device.key_press(b'x')
        log.log_info("获胜：拾取物品...")
        return ql_type.goods
    elif cnt > 9:
        log.log_info("获胜：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("获胜：等待{cnt}尝试...")
        return do_win(img, points, cnt+1)


def do_goods(img, points, cnt = 0):
    '''
    捡物品
    '''
    if point_judge(points, 'ql_order'):
        # device.key_press(b'space')
        log.log_info("捡物品：进入对战表,已按下Space...")
        return ql_type.order
    elif point_judge(points, 'ql_ready1') or point_judge(points, 'ql_ready2'):
        # device.key_press(b'space')
        log.log_info("捡物品：进入准备，已按下Space...")
        return ql_type.ready
    elif judeg_goods(points):
        # device.key_press(b'x')
        log.log_info("捡物品：拾取物品...")
        return ql_type.goods
    elif cnt > 9:
        log.log_info("捡物品：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("捡物品：等待{cnt}尝试...")
        return do_goods(img, points, cnt+1)


def do_end(img, points, cnt=0):
    '''
    结算
    '''
    if point_judge(points, 'ql_end'):
        log.log_info("结算：结算中...")
        return ql_type.end
    elif point_judge(points, 'ql_next'):
        log.log_info("结算：是否再次...")
        return ql_type.next
    elif cnt > 9:
        log.log_info("结算：未知...")
        copy_img()
        return ql_type.unknow
    else:
        img = get_img()
        log.log_info("结算：等待{cnt}尝试...")
        return do_end(img, points, cnt+1)

    next = 13    # 继续
    out = 14     # 退出
    sell = 14    # 售卖
def do_next(img, points):
    '''
    继续
    '''
    global over_cnt
    lif point_judge(points, 'ql_next'):
        if over_cnt >= 10 and random.randint(0, 4) == 0:
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



def do_quite(points):
    '''
    退出
    '''
    if point_judge(points, 'ql_out'):
        device.mouse_move(100, 100)
        device.mouse_left_click()
        log.log_info("Out：Start Sell...")
        return ql_type.sell
    elif point_judge(points, 'ql_next'):
        log.log_info("Next：等待...")
        return ql_type.next
    for i in range(1, 10):
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


def get_img():
    user32.get_pic(hwnd, 'dnf')
    return cv2.imread(r'img/dnf.jpg')


def copy_img():
    '''
    复制图片
    '''
    shutil.copy('img\\dnf.jpg', 'img\\' +
                datetime.now().strftime('%Y%m%d%H%M%S%f') + '.jpg')
