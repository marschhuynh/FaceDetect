import numpy as np
import cv2

model = cv2.CascadeClassifier('model/stop_sign.xml')

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set width 
cam.set(4, 480) # set height

while (True):
    rval, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    obj_detected = model.detectMultiScale(gray, 1.3, 5)
    obj_detected2 = model2.detectMultiScale(gray, 1.3, 5)

    if (len(obj_detected) >= 1):
        print(obj_detected)
    for (x, y, w, h) in obj_detected:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Preview', img)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
