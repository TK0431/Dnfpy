import utility.key as key
import win32api
import time

time.sleep(3)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)
win32api.keybd_event(65,0x1e,0,0)
time.sleep(1)



import cv2
import numpy as np
import win32gui
import win32ui
import win32con
import win32api


def grab_screen(region=None):
    #### for manual region grab ######

    hwin = win32gui.GetDesktopWindow()

    if region:
        left, top, x2, y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return img



# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: CSD
# @Date  : 2020/1/27 0027 16:05
# @Software: PyCharm
from aip import AipOcr
import time
from ctypes import *
import cv2
from grabscreen import grab_screen

JianShulib = CDLL("./msdk.dll", RTLD_GLOBAL)
h = JianShulib.M_Open_VidPid(0x612c, 0x1030)

""" 你的 APPID AK SK """
APP_ID = '15660906'
API_KEY = '1K7CqMsW2QukaaD4kqVYcm5P'
SECRET_KEY = 'KuQkFfaS1i8dA0RCPdmUeKHnDcKEuyVP'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 移动到门口
def move_to():
    # 出门
    time.sleep(2)
    JianShulib.M_KeyDown2(h, 40)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 40)
    # 打开地图
    JianShulib.M_KeyDown2(h, 78)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 78)
    # 点击地图
    JianShulib.M_MoveTo(h, 490, 360)
    time.sleep(2)
    JianShulib.M_LeftClick(h, 1)
    time.sleep(5)
    # 进图
    JianShulib.M_KeyDown2(h, 39)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 39)
    # 选图青龙
    JianShulib.M_MoveTo(h, 210, 550)
    time.sleep(2)
    JianShulib.M_LeftClick(h, 3)
    time.sleep(4)
    # 跳过
    JianShulib.M_KeyDown2(h, 32)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 32)


# 攻击
def auto_attack(k=0):
    if k == 0:
        for i in range(2):
            time.sleep(0.5)
            JianShulib.M_KeyDown2(h, 65)  # a
            time.sleep(1)
            JianShulib.M_KeyUp2(h, 65)
            time.sleep(0.3)
            JianShulib.M_KeyDown2(h, 88)  # x
            time.sleep(1)
            JianShulib.M_KeyUp2(h, 88)
            time.sleep(0.3)
            JianShulib.M_KeyDown2(h, 83)  # s
            time.sleep(0.5)
            JianShulib.M_KeyUp2(h, 83)
            time.sleep(0.5)
            JianShulib.M_KeyDown2(h, 68)  # d
            time.sleep(0.5)
            JianShulib.M_KeyUp2(h, 68)
            # JianShulib.M_KeyDown2(h, 81)  # q
            # JianShulib.M_KeyUp2(h, 81)
            # JianShulib.M_KeyDown2(h, 87)  # w
            # JianShulib.M_KeyUp2(h, 87)
            # JianShulib.M_KeyDown2(h, 69)  # e
            # JianShulib.M_KeyUp2(h, 69)
    else:
        return


# 捡物品
def get_wupin():
    JianShulib.M_KeyDown2(h, 162)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 162)
    JianShulib.M_KeyDown2(h, 88)
    time.sleep(3)
    JianShulib.M_KeyUp2(h, 88)


# 换角色
def change_role():
    # 按ESC选择角色
    JianShulib.M_KeyDown2(h, 27)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 27)
    JianShulib.M_MoveTo(h, 480, 580)
    time.sleep(2)
    JianShulib.M_LeftClick(h, 1)
    time.sleep(1)
    # 选择另外一个角色
    JianShulib.M_KeyDown2(h, 39)
    time.sleep(1)
    JianShulib.M_KeyUp2(h, 39)
    JianShulib.M_KeyDown2(h, 32)
    time.sleep(2)
    JianShulib.M_KeyUp2(h, 32)


# 回城
def get_back():
    JianShulib.M_KeyDown2(h, 27)
    time.sleep(1)
    JianShulib.M_KeyUp2(h, 27)
    JianShulib.M_MoveTo(h, 645, 573)
    time.sleep(2)
    JianShulib.M_LeftClick(h, 1)
    time.sleep(1)
    JianShulib.M_KeyDown2(h, 27)
    time.sleep(1)
    JianShulib.M_KeyUp2(h, 27)
    change_role()


# 获取图片路径
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


pilao = 188
while True:
    print(pilao)
    if h != -1:
        JianShulib.M_MoveTo2(h, 500, 715)
        time.sleep(0.5)
        JianShulib.M_MoveTo2(h, 550, 715)
        screen = cv2.resize(grab_screen(region=(0, 0, 1024, 768)), (800, 600))
        cv2.imwrite('000.png', screen)
        image = get_file_content('000.png')
        """ 调用通用文字识别, 图片参数为本地图片 """
        result = client.basicAccurate(image)  # basicAccurate精确 basicGeneral基本
        result = result['words_result']
        print(result)
        words = ''
        for i in result:
            words = words + i['words']
        # print(words)
        if pilao <= 0:
            get_back()
            pilao = 188
        elif '是否继续' in words:
            get_wupin()
            JianShulib.M_KeyDown2(h, 121)
            time.sleep(2)
            JianShulib.M_KeyUp2(h, 121)
            time.sleep(7)
            JianShulib.M_KeyDown2(h, 32)
            time.sleep(2)
            JianShulib.M_KeyUp2(h, 32)
            pilao = pilao - 8
        elif '尔文防线' in words:  # or '亚' in words：
            move_to()
            pilao = pilao - 8
        else:
            flag = JianShulib.M_CapsLockLedState(h)
            print('state:%s' % flag)
            if flag == 0:
                auto_attack(k=flag)
            else:
                print('end')
                break
    else:
        print('请插入设备')
        break
