import utility.opencv as opencv
import utility.user32 as user32
from functools  import wraps
import time

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
def get():
    user32.get_win_rgb(5,5)
    hwnd = user32.get_hwnd('Send Message')
    print(user32.set_win_pos(hwnd))
    print(user32.get_mouse_pos())

get()

