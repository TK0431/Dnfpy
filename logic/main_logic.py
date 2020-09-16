import utility.key as key
import win32api

def main_start(hwnd):
    key.send_space()
    key.send_down(2)
    key.send_space()
    key.send_num_key(1)
    key.send_enter(2)
    key.send_keys('x', num=3)


def press_key(self, character=''):
    """
    Press a given character key.
    """
    try:
        shifted = self.is_char_shifted(character)
    except AttributeError:
        win32api.keybd_event(character, 0, 0, 0)
    else:
        if shifted:
            win32api.keybd_event(self.shift_key, 0, 0, 0)
        char_vk = win32api.VkKeyScan(character)
        win32api.keybd_event(char_vk, 0, 0, 0)


def release_key(self, character=''):
    """
    Release a given character key.
    """
    try:
        shifted = self.is_char_shifted(character)
    except AttributeError:
        win32api.keybd_event(character, 0, KEYEVENTF_KEYUP, 0)
    else:
        if shifted:
            win32api.keybd_event(self.shift_key, 0, KEYEVENTF_KEYUP, 0)
        char_vk = win32api.VkKeyScan(character)
        win32api.keybd_event(char_vk, 0, KEYEVENTF_KEYUP, 0)
