import xml.etree.ElementTree as ET

xml_file = 'files/step.xml'

def get_value():
    '''
    获取执行状态
    '''
    tree = ET.parse(xml_file)
    root = tree.getroot()

    date = root.find('date').get('value')
    user = root.find('user').get('value')
    cnt = int(root.find('cnt').get('value'))
    state = root.find('state').get('value')
    return date, user, cnt, state

def set_value(date, user, cnt, state):
    '''
    设置执行状态
    '''
    tree = ET.parse(xml_file)
    root = tree.getroot()

    root.find('date').set('value',date)
    root.find('user').set('value',user)
    root.find('cnt').set('value',str(cnt))
    root.find('state').set('value',state)

    tree.write(xml_file)
