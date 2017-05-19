from PIL import Image
import face_recognition
import cv2
import dlib

model = "shape_predictor_68_face_landmarks.dat"
landmarks_obj = dlib.shape_predictor(model)
faces = dlib.get_frontal_face_detector()
win = dlib.image_window()


img = cv2.imread('test_image/face6.jpg')
rect = faces(img)
win.set_image(img)

for i , d in enumerate(rect, 1):
    # cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (0,255,0), 2)
    win.add_overlay(d)
# cv2.imshow("test frame ", img)
# cv2.waitKey(100000)
dlib.hit_enter_to_continue()

# # Load the jpg file into a numpy array
# image = face_recognition.load_image_file("test_image/face1.jpg")
#
# # Find all the faces in the image
# face_locations = face_recognition.face_locations(image)
#
# print("I found {} face(s) in this photograph.".format(len(face_locations)))
#
# for face_location in face_locations:
#
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#
#     # You can access the actual face itself like this:
#     cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
# cv2.imshow("video", image)

