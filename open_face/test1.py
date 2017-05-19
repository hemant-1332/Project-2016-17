import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture(1)
cv2.namedWindow('Video Feed', cv2.WINDOW_AUTOSIZE)
success,image = vidcap.read()
count = 0
timer = 1
success = True
folder = 'person'
while success:
  success,image = vidcap.read()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  print 'Read a new frame: ', success
  if timer%5==0:
      cv2.imwrite('frame%d.jpg' % count, image)     # save frame as JPEG file
      print 'inside timer'
  cv2.imshow('Videp Feed', image)
  count += 1
  timer+=1
  key = cv2.waitKey(10) & 0xff
  if key ==27:
      break
vidcap.release()
cv2.destroyAllWindows()