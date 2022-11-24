import cv2
import time

start = time.time()

cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    cv2.imshow('camera', img)
    if cv2.waitKey(1) == 27:
        break
end = time.time()


print(end - start)
cam.release()
cv2.destroyAllWindows()