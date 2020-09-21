
import ctypes as C
import time
import random
import utility.log as log

msdk = C.WinDLL(r'dll\kmllib.dll')

def open_device(vender_id=0, product_id=0):
    '''
    打开设备
    vender_id:设备的厂商ID
    product_id:产品ID
    '''
    if check_device(): return True

    if vender_id != 0 or product_id != 0:
        if msdk.OpenDeviceEx(vender_id, product_id) == 1:
            log.log_info('打开指定ID设备成功！')
        else:
            log.log_error("打开指定ID设备失败！")
            return -1
    else:
        if msdk.OpenDevice() == 1:
            log.log_info('打开设备成功！')
        else:
            log.log_error('打开设备失败！')
            return -1

    return check_device()

def check_device():
    '''
    设备检查
    '''
    if msdk.CheckDevice() == 1:
        log.log_info('设备已连接！')
        return True
    else:
        log.log_info('设备未连接！')
        return False

def close_device():
    '''
    关闭设备
    '''
    msdk.CloseDevice()
    log.log_info('关闭设备！')


def restart_device(sed=0):
    '''
    重启设备
    sed:延时启动时间
    '''
    if sed > 0:
        msdk.Disconnect(sed)
    else:
        msdk.Restart()
    log.log_info('重启设备！')


def set_device_id(vender_id, product_id):
    '''
    修改设备ID(65535)
    '''
    if msdk.SetDeviceID("", vender_id, product_id) == 1:
        log.log_info("修改设备ID成功！")
        restart_device()
    else:
        log.log_error("修改设备ID失败")


def default_device_id():
    '''
    恢复设备默认ID
    '''
    msdk.RestoreDeviceID("")


def get_info_device():
    '''
    获取:序列号,型号,版本号,出厂日期
    '''
    return get_str(msdk.GetSN()), get_str(msdk.GetModel()), get_str(msdk.GetVersion()), get_str(msdk.GetProductionDate())


def get_str(str):
    return C.string_at(str).decode('utf-8')


def get_sleep(slp):
    time.sleep(slp * random.uniform(0.9, 1.1))


def key_down(key, slp=0.05):
    get_sleep(slp)
    msdk.KeyDown(key)


def key_up(key, slp=0.05):
    get_sleep(slp)
    msdk.KeyUp(key)


def key_press(key, cnt=1, slp=0.05):
    for cnt in range(0, cnt):
        get_sleep(slp)
        key_down(key, slp)
        key_up(key, slp)


def get_pos(x,y,x_r,y_r):
    x += x_r * random.uniform(-1,1)
    y += y_r + random.uniform(-1,1)
    return x, y


def mouse_move(x,y,x_r,y_r):
    x,y = get_pos(x,y)
    msdk.SimulationMove(x,y)


def mouse_left_down(slp=0.1):
    get_sleep(slp)
    msdk.LeftDown()


def mouse_left_up(slp=0.1):
    get_sleep(slp)
    msdk.LeftUp()


def mouse_left_click(cnt=1, slp=0.05):
    for cnt in range(0, cnt):
        slp = get_sleep(slp)
        msdk.mouse_left_down(slp)
        msdk.mouse_left_up(slp)


