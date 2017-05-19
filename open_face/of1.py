import sys
import dlib
from skimage import io
import cv2
import numpy

# Take the image file name from the command line
#file_name = sys.argv[1]
file_name = "test2.jpg"
# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

# Load the image into an array
#image = io.imread(file_name)
cap_object = cv2.VideoCapture()
while True:
    ret, image = cap_object.read()
    detected_faces = face_detector(image, 1)
    win.set_image(image)

    for i, face_rect in enumerate(detected_faces):
        print ("found")
        win.add_overlay(face_rect)

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cap_object.release()
cv2.destroyAllWindows()



# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the sample_faces in our image.
#detected_faces = face_detector(image, 1)

#print("I found {} sample_faces in the file {}".format(len(detected_faces), file_name))

# Open a window on the desktop showing the image
#win.set_image(image)

# Loop through each face we found in the image
# for i, face_rect in enumerate(detected_faces):
#     # Detected sample_faces are returned as an object with the coordinates
#     # of the top, left, right and bottom edges
#     print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),
#                                                                              face_rect.right(), face_rect.bottom()))
#
#     # Draw a box around each face we found
#     win.add_overlay(face_rect)
#
# # Wait until the user hits <enter> to close the window
# dlib.hit_enter_to_continue()