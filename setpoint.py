import xml.etree.ElementTree as ET
import cv2

tree = ET.parse(r'files/points.xml')
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
            pic = point.get('pic')
            set_pos('img\\'+ pic +'.png',point)

tree.write(r'files/points_2.xml')
