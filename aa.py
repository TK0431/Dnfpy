
import ctypes as C
import cv2
import time
import random
import utility.device as device
import utility.user32 as user32
import utility.opencv as opencv

# img = user32.get_win_rgbs(70,807)
# cv2.imshow('test', img)
# cv2.waitKey(0)

while True:
    time.sleep(1)
    user32.print_mouse_pos()

# 1080 * 1920
# img = cv2.imread('img/1.png')
# img2 = img[757:787,62:92,:]
# cv2.imshow('test',img2)
# cv2.waitKey(0)

# hwnd = user32.get_hwnd('AutoTest')
# print(user32.set_win_pos(hwnd))