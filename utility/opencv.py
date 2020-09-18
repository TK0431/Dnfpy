import cv2
import numpy as np
import utility.user32 as user32

def show_win_range(x,y,w,h):
    img = user32.get_win_rgbs(x,y,w,h)
    cv2.imshow('one',img)
    cv2.waitKey()
