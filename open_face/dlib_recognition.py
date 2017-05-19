import face_recognition
import cv2
# import socket

# client = socket.socket()
# client.connect(("172.17.27.157",12345))

def calc_track_loc(top, left, bottom, right):
    track_x = (left + right) / 2
    track_y = (top + bottom) / 2
    return (track_x, track_y)


def sending_information(track_locs, face_names):
    sending_info = str(zip(track_locs, face_names))
    print sending_info
    # client.send(sending_info)

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect sample_faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
sample_image = face_recognition.load_image_file("sample_faces/hemant.jpg")
jatin_image = face_recognition.load_image_file("sample_faces/jatin.jpg")
sample_face_encoding = face_recognition.face_encodings(sample_image)[0]
jatin_encoding = face_recognition.face_encodings(jatin_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = 0

while True:
    track_locs = []
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25, interpolation = cv2.INTER_AREA)

    # Only process every other frame of video to save time
    if process_this_frame%10==0:
        # Find all the sample_faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame) # list of faces locations # Face detection Algo 1
        face_encodings = face_recognition.face_encodings(small_frame, face_locations) # list of face encoding arrays # Face encoding extraction Algo 2
qqq
        face_names = []
        for face_encoding in face_encodings: # face encoding is a 1x128 array
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([sample_face_encoding, jatin_encoding], face_encoding) # Encoding comparison Algo 3
            name = "Unknown"

            if match[0]:
                name = "Hemant"
            if match[1]:
                name = "Jatin"

            face_names.append(name)

    process_this_frame += 1


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        track_locs.append(calc_track_loc(top, left, bottom, right))
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) # Blue Rectangle with thickness 2

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom  - 6), font, 1.0, (255, 255, 255), 1)

    if process_this_frame%5==0:
        sending_information(track_locs, face_names)


    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

