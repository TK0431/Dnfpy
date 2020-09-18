
import ctypes as C
import time
import random
import utility.log as log

msdk = C.CDLL(r'dll\kmllib64.dll')


def check(vender_id=0, product_id=0):
    '''
    打开设备
    vender_id:设备的厂商ID
    product_id:产品ID
    '''
    if msdk.CheckDevice() == 1:
        log.log_info('设备已连接！')
    else:
        log.log_error('设备未连接！')
        return -1

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
    return msdk.GetSN(), msdk.GetModel(), msdk.GetVersion(), msdk.GetProductionDate()


def get_sleep(slp):
    time.sleep(slp * 1.1 * random.uniform(-1, 1))


def key_down(key, slp=0.1):
    get_sleep(slp)
    msdk.KeyDown(key)


def key_up(key, slp=0.1):
    get_sleep(slp)
    msdk.KeyUp(key)


def key_press(key, cnt=1, slp=0.1):
    for cnt in range(0, cnt):
        slp = get_sleep(slp)
        msdk.key_down(key, slp)
        msdk.key_up(key, slp)


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


def mouse_left_click(cnt=1, slp=0.1):
    for cnt in range(0, cnt):
        slp = get_sleep(slp)
        msdk.mouse_left_down(slp)
        msdk.mouse_left_up(slp)


