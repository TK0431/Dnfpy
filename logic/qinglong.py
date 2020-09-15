import utility.key as key



def skill1(hwnd):
    key.send_down(2)
    key.send_space()

def skip_event():
    key.send_space()

def move_goods():
    key.send_num_key(1)

def get_goods():
    key.send_key('x')