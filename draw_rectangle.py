import numpy as np
import cv2

# details of rectangle to be drawn.
x, y, h, w = (493, 305, 125, 90)

cap = cv2.VideoCapture(2)
s, img = cap.read()

while s:
  ret, frame = cap.read()
  
  # draw a rectangle.
  cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

  # show it ;)
  cv2.imshow('img', frame)
  
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "fin."
