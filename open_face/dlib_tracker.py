import os
import dlib
import glob
import cv2
import get_points

cam = cv2.VideoCapture(0)


while True:
    retval, img = cam.read()
    print ('inside 1')

    if cv2.waitKey(10) & 0xff==ord('p'):
        break

    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", img)

cv2.destroyAllWindows()

points = get_points.run(img)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", img)

tracker = dlib.correlation_tracker()

tracker.start_track(img, dlib.rectangle(*points[0]))

while True:

    retval, img = cam.read()

    tracker.update(img)
    # Get the position of the object, draw a
    # bounding box around it and display it.
    rect = tracker.get_position()
    pt1 = (int(rect.left()), int(rect.top()))
    pt2 = (int(rect.right()), int(rect.bottom()))
    cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
    print "Object tracked at [{}, {}] \r".format(pt1, pt2),

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    # Continue until the user presses ESC key
    if cv2.waitKey(1) == 27:
        break