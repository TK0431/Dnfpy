import cv2

image = cv2.imread('222.jpg')
faceCascade = cv2.CascadeClassifier('files/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5,minSize =(5,5))

print(faces)
print("find{0}".format(len(faces)))

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+w), (0,255,0), 2)
cv2.imshow('dect',image)
cv2.waitKey(0)
cv2.destroyAllWindows()