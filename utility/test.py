import cv2
import time
from functools  import wraps

def timefn(fn):
    @wraps(fn)
    def get_diff_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f'@timefn: {fn.__name__} took {t2 - t1: .5f} s')
        return result

    return get_diff_time