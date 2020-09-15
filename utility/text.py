import cv2
import pytesseract
import time
from functools  import wraps

from PIL import Image

def timefn(fn):
    @wraps(fn)
    def get_diff_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f'@timefn: {fn.__name__} took {t2 - t1: .5f} s')
        return result

    return get_diff_time

@timefn
def get_text(pic):
    img = cv2.imread(pic)
    #im2=Image.open(pic)
    text=pytesseract.image_to_string(img, lang='chi_sim')
    print(text)


get_text(r'E:\GitHub\Dnfpy\utility\test.png')
#get_text(r'E:\GitHub\Dnfpy\utility\test3.jpg')