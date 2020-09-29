import xml.etree.ElementTree as ET
import cv2

tree = ET.parse(r'files/points_bk.xml')
root = tree.getroot()

def set_pos(pic,point):
    img = cv2.imread(pic)
    for pos in point.findall('pos'):
        x =int(pos.get('x'))
        y =int(pos.get('y'))
        b =img[y,x,0]
        g =img[y,x,1]
        r = img[y,x,2]
        pos.set('r', str(r))
        pos.set('g', str(g))
        pos.set('b', str(b))

groups = root.findall('group')
for group in groups:
    if group.get('value') == 'ql':
        points = group.findall('point')
        for point in points:
            if point.get('value') == 'ql_jd':
                set_pos(r'img\3.png',point)
            elif point.get('value') == 'ql_dzb':
                set_pos(r'img\4.png',point)
            elif point.get('value') == 'ql_door':
                # set_pos(r'img\3.png',point)
                pass
            elif point.get('value') == 'ql_f10':
                set_pos(r'img\2.png',point)
            elif point.get('value') == 'ql_zb_1':
                set_pos(r'img\5.png',point)
            elif point.get('value') == 'ql_zb_1':
                set_pos(r'img\6.png',point)

tree.write(r'files/points.xml')
