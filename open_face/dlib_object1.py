import dlib
from skimage import io
import cv2

options = dlib.simple_object_detector_training_options()

detector = dlib.simple_object_detector("sign_detector.svm")

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 720)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)


while True:
    ret, frame = cam.read()
    rect = detector(frame)
    for i , d in enumerate(rect, 1):
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0,255,0), 2)


    cv2.imshow("frame ", frame)

    if cv2.waitKey(10) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()

