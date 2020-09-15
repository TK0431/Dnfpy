import cv2
import time
from functools  import wraps

from PIL import Image

def timefn(fn):
    @wraps(fn)
    def get_diff_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f'@timefn: {fn.__name__} took {t2 - t1: .5f} s')
        return result

    return get_diff_time

@timefn
def get_test():
    image = cv2.imread(r'E:\GitHub\Dnfpy\train\test.png')
    faceCascade = cv2.CascadeClassifier(r'E:\GitHub\Dnfpy\train\s1\cascade.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 10,minSize =(30,30))

    print(faces)
    print("find{0}".format(len(faces)))

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+w), (0,255,0), 2)
    cv2.imshow('dect',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

get_test()