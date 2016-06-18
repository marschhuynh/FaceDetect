import cv2

cv2.namedWindow("preview")
cam = cv2.VideoCapture(0)

cam.set(3,320) # set width 
cam.set(4,240) # set height

if cam.isOpened(): # try to get the first frame
    rval, frame = cam.read()
else:
    rval = False

frame = cv2.flip(frame,2)
cv2.imshow("preview", frame)
cam.release()

while (True):
    # cv2.imshow("preview", frame)
    # rval, frame = cam.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")