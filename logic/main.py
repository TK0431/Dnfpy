import utility.device as device
import logic.ql as ql
import utility.user32 as user32

def start(key,value,name,cnt,envent):
    if envent == 'ql':
        ql.start(key,value,name,cnt)
    else:
        pass
