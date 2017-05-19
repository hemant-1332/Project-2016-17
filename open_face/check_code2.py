import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('test_image/face6.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))
for (x,y,w,h) in faces:
    img = cv2.rectangle(gray,(x,y),(x+w,y+h),(225,0,0),2)


cv2.imshow("faces",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()