import time
import utility.start as start
import utility.user32 as user32

full_path = ''
name = '地下城与勇士'

if __name__ == "__main__":
    cnt = 0
    while True:
        time.sleep(1)
        print('Count : ' + str(cnt))

        hwnd = user32.get_hwnd(name)
        if hwnd == 0:
            hwnd = start.start_exe(name,full_path)
            if hwnd == 0:
                break
        print(hwnd)

        cnt += 1
