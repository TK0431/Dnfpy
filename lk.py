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
# user32.get_pic(hwnd,'3')
#print(user32.get_win_pos(hwnd))

img = cv2.imread('img\\3.png')
# # x,y =4,2
x1,y1 = 1098,56
# x2,y2 = 543,389
# x3,y3 = 640,389
print(img[y1,x1,2],img[y1,x1,1],img[y1,x1,0])
# print(img[y2,x2,2],img[y2,x2,1],img[y2,x2,0])
# print(img[y3,x3,2],img[y3,x3,1],img[y3,x3,0])


img = cv2.imread(r'img\2.png')
print(img[y1,x1,2],img[y1,x1,1],img[y1,x1,0])


# print(user32.get_win_rgb(1099+4,57+2))

# for i in range(1090,1110):
#     for j in range(47,67):
#         r,g,b =user32.get_win_rgb(i,j)
#         if r==204 and g==180 and b==154:
#             print(i,j)