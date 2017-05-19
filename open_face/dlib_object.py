import dlib
from skimage import io


options = dlib.simple_object_detector_training_options()
#print options.C
options.C = 5
options.num_threads = 4
options.be_verbose = True

dlib.train_simple_object_detector("cat.xml", "cat.svm", options)

# print("Training accuracy: {}".format(
#     dlib.test_simple_object_detector("object1.xml", "object1.svm")))

# detector = dlib.simple_object_detector("sign_detector.svm")
#
# # win_det = dlib.image_window()
# # win_det.set_image(detector)
#
# win = dlib.image_window()
# img = io.imread("traffic.jpg")
# dets = detector(img)
#
# win.set_image(img)
# win.add_overlay(dets)
# dlib.hit_enter_to_continue()