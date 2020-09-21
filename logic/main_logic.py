import utility.device as device
import utility.user32 as user32

def main_start(hwnd):
    device.open_device()
    device.key_press(b'a')
    device.key_press(b'space')
    device.key_press(b'down',cnt = 2)
    device.key_press(b'space')
    device.key_press(b'num1')
    device.key_press(b'enter')
    device.key_press(b'x', cnt=3)

