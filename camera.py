import cv2

cv2.namedWindow("Camera")
cam = cv2.VideoCapture(0)

cam.set(3, 320) # set width 
cam.set(4, 240) # set height

if cam.isOpened(): # try to get the first frame
    rval, frame = cam.read()
else:
    rval = False

frame = cv2.flip(frame, 2)

while (True):
    rval, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Camera', img)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        cam.release()
        break

cv2.destroyWindow("Camera")
