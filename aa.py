
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

# while True:
#     time.sleep(1)
#     x,y = user32.get_mouse_pos()
#     r,g,b = user32.get_win_rgb(x,y)
#     print(x,y,r,g,b)
#     img = np.zeros((100,100,3),dtype=np.uint8)
#     img[:,:,0] = b
#     img[:,:,1] = g
#     img[:,:,2] = r
#     cv2.imshow('test',img)
#     cv2.waitKey(1000)

# 1080 * 1920
# img = cv2.imread('img/1.png')
# img2 = img[757:787,62:92,:]
# cv2.imshow('test',img2)
# cv2.waitKey(0)

# hwnd = user32.get_hwnd('地下城与勇士')
# print(user32.get_win_pos(hwnd))


img = cv2.imread(r'D:\7.png')
x,y =16,13
# x1,y1 = 500,710
# x2,y2 = 500,770
# x3,y3 = 500,880
# x1,y1 = 80,1388
# x2,y2 = 80,1408
# x3,y3 = 80,1429
# x1,y1 = 835,928
# x2,y2 = 835,938
# x3,y3 = 835,948
x1,y1 = 503,790
x2,y2 = 503,815
x3,y3 = 503,835
print(img[x1,y1,2],img[x1,y1,1],img[x1,y1,0])
print(img[x2,y2,2],img[x2,y2,1],img[x2,y2,0])
print(img[x3,y3,2],img[x3,y3,1],img[x3,y3,0])