
import ctypes as C
import cv2
import time
import random
import numpy as np
import utility.device as device
import utility.user32 as user32
import utility.opencv as opencv

# img = user32.get_win_rgbs(70,807)
# cv2.imshow('test', img)
# cv2.waitKey(0)

while True:
    time.sleep(1)
    x,y = user32.get_mouse_pos()
    r,g,b = user32.get_win_rgb(x,y)
    print(x,y,r,g,b)
    img = np.zeros((100,100,3),dtype=np.uint8)
    img[:,:,0] = b
    img[:,:,1] = g
    img[:,:,2] = r
    cv2.imshow('test',img)
    cv2.waitKey(1000)

# 1080 * 1920
# img = cv2.imread('img/1.png')
# img2 = img[757:787,62:92,:]
# cv2.imshow('test',img2)
# cv2.waitKey(0)

# hwnd = user32.get_hwnd('AutoTest')
# print(user32.set_win_pos(hwnd))