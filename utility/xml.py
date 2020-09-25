import xml.etree.ElementTree as ET
import time

xml_step_file = 'files/step.xml'


def get_step_value():
    '''
    获取step.xml执行状态
    '''
    tree = ET.parse(xml_step_file)
    root = tree.getroot()

    date = root.find('date').get('value')
    user = root.find('user').get('value')
    cnt = root.find('cnt').get('value')
    return date, user, cnt


def set_step_value(date, user, cnt):
    '''
    设置step.xml执行状态
    '''
    tree = ET.parse(xml_step_file)
    root = tree.getroot()

    root.find('date').set('value', date)
    root.find('user').set('value', user)
    root.find('cnt').set('value', str(cnt))

    tree.write(xml_step_file)


xml_users_file = 'files/users.xml'


def get_users_value():
    '''
    获取users数据
    '''
    tree = ET.parse(xml_users_file)
    root = tree.getroot()

    date, user, cnt  = get_step_value()
    today = time.strftime("%Y%m%d", time.localtime())
    flg = False if date == today else True

    users = {}
    ids = root.findall('id')
    for i in ids:
        key = i.get('value')
        users.setdefault(key, [])
        roles = i.findall('role')
        for role in roles:
            if flg :
                users[key].append((role.get('value'), role.get('name'), role.get(
                    'cnt'), role.get('event')))
            else:
                if user == role.get('value') and cnt == role.get('cnt'):
                    flg = True

    return users


xml_points_file = 'files/points.xml'


def get_points_value(group_key):
    '''
    获取points数据
    '''
    tree = ET.parse(xml_points_file)
    root = tree.getroot()
    points = {}
    grp = root.findall('group')
    for g in grp:
        group_key = g.get('value')
        if group_key == group_key:
            pts = g.findall('point')
            for p in pts:
                key = p.get('value')
                points.setdefault(key, [])
                poss = p.findall('pos')
                for pos in poss:
                    points[key].append((pos.get('x'), pos.get(
                        'y'), pos.get('r'), pos.get('g'), pos.get('b')))

    return points
