import cv2
import SimpleCV
import numpy as np

def takePhoto():
    try:
        mylaptopcam = SimpleCV.Camera(1, prop_set = {"width": 1280, "height": 720})
        d = mylaptopcam.getImage()        
        d.save("captura.jpg")        
        print('listo!!')
    except Exception as ex:
        print('Unhandled error: ' + ex)
    finally:
        del mylaptopcam


#xml classifiers.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cam = cv2.VideoCapture(2)
s, img = cam.read()

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

while s:

  s, img = cam.read()
  gray = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      print 'captura cara.'
      #takePhoto()
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray)
      for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
          print 'captura ojos.'
          #takePhoto()

  cv2.imshow(winName,img)
  
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "fin."
