import logging
from datetime import datetime

# Log 配置
log_format = '%(asctime)s : %(levelname)s  %(message)s'
log_file = 'log/log_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.log'
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format=log_format,
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode = 'w')

def log_console_start():
    '''
    控制台 Log
    '''
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter(log_format)  # 定义该handler格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)  # 实例化添加handler

def log_debug(msg):
    '''
    测试 Log
    '''
    logging.debug(msg)

def log_info(msg):
    '''
    正常 Log
    '''
    logging.info(msg)

def log_warn(msg):
    '''
    警告 Log
    '''
    logging.warning(msg)

def log_error(msg):
    '''
    异常 Log
    '''
    logging.error(msg)
