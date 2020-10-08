# 测试文件，无用
import cv2
import datetime
import utility.device as device
import time


r = 179
g = 107
b = 255

col_step = 50
row_step = 15


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
    #if r == 103 and g == 211 and b == 235: return True
    return False


print(datetime.datetime.now())
img = cv2.imread('img\\8.png')
print(judeg_goods(img))
print(datetime.datetime.now())


import random

def sell_goods(img):
    '''
    分解
    '''
    # 点击分解机
    y = random.randint(380,480)
    x = 0
    for x0 in range(277,435):
        bb = img[427,x0,0]
        gg = img[427,x0,1]
        rr = img[427,x0,2]
        if 234 < rr and rr < 244 and 225 < gg and gg < 235 and 216 < bb and bb < 226:
            x = x0
            break
    if x > 0:
        x = x - random.randint(0,160)
    else:
        x = x - random.randint(251,271)
    print(x,y)
    device.mouse_move(x,y)
    device.mouse_left_click()

    # 点击二级菜单“分解装备”
    time.sleep(0.5)
    x = x + 4 + random.randint(0,91)
    y = y+ 42 + random.randint(0,13)
    print(x,y)
    device.mouse_move(x,y)
    device.mouse_left_click()
    time.sleep(0.5)

    # 获取最新图片
    # img = get_img()

    # 点击全选
    x = random.randint(450,558)
    y = random.randint(335,350)
    device.mouse_move(x,y)
    device.mouse_left_click()
    time.sleep(0.5)

    # 获取最新图片
    # img = get_img()

    # if None

    # 点击分解
    x = random.randint(541,588)
    y = random.randint(467,483)
    device.mouse_move(x,y)
    device.mouse_left_click()


# device.open_device()
# time.sleep(2)
# img = cv2.imread('img\\s1.png')
# sell_goods(img)

