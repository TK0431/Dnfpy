import cv2
import os

size = 30
base_path = 'train\\'
base = 'E:\\GitHub\\Dnfpy\\train\\'
in_path = 's1_in\\'
out_path = 's1_out\\'
no_path = 's1_no\\'
f_name = 'pos.txt'
n_name = 'neg.txt'

files = os.listdir(base_path + in_path)
with open(base_path + f_name,'w',encoding='utf-8') as f:
    for fi in files:
        if fi.endswith('jpg') or fi.endswith('png'):
            img = cv2.imread(base_path + in_path + fi)
            img = cv2.resize(img,(size,size))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(base_path + out_path + fi,img)
            f.write(out_path + fi + ' 1 0 0 ' + f'{size} {size}\n')

files = os.listdir(base_path + no_path)
with open(base_path + n_name,'w',encoding='utf-8') as f:
    for fi in files:
        if fi.endswith('jpg') or fi.endswith('png'):
            f.write(base + no_path + fi + '\n')

# opencv_createsamples.exe -vec E:\GitHub\Dnfpy\train\pos.vec -info E:\GitHub\Dnfpy\train\pos.txt -num 20 -w 30 -h 30
# opencv_traincascade.exe -data E:\GitHub\Dnfpy\train -vec E:\GitHub\Dnfpy\train\pos.vec -bg E:\GitHub\Dnfpy\train\neg.txt -numPos 1 -numNeg 20 -numstages 10 -featureType LBP -w 30 -h 30

