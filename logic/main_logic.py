import utility.key as key

def main_start(hwnd):
    key.send_space()
    key.send_down(2)
    key.send_space()
    key.send_num_key(1)
    key.send_enter(2)
    key.send_keys('x',num= 3)