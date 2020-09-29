import cv2
import numpy as np
import utility.user32 as user32

def show_win_range(x,y,w,h):
    img = user32.get_win_rgbs(x,y,w,h)
    cv2.imshow('one',img)
    cv2.waitKey()

def show_rgb(r,g,b):
    img = np.zeros((200,200,3),dtype=np.uint8)
    img[:,:,0]=b
    img[:,:,1]=g
    img[:,:,2]=r
    cv2.imshow('rgb',img)
    cv2.waitKey(img)

def save_img(points):
    tm = '20190101'
    cv2.imwrite(f'img\\{tm}.png',points)