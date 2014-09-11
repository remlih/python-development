import cv2
import cv2.cv as cv
import numpy as np
import os.path

winName = 'Image display'
cameraIndex = 2
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

camera = cv.CaptureFromCAM(cameraIndex)
video = cv2.VideoCapture(cameraIndex);
##video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 720)
##video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

newImage = 'images\ZnewImage.jpg'
previousImage = 'images\ZpreviousImage.jpg'
modelImage = 'images\Zmodel.jpg'
isNew = True

while True:
    #enable camera and display image.
    isRunning, imageNormal = video.read()
    imageGray = cv2.cvtColor(imageNormal, cv2.COLOR_RGB2GRAY)    
    image = cv.QueryFrame(camera)
    cv2.imshow(winName, imageGray)

    #save image in hd.
    if (isNew == True):
        cv2.imwrite(newImage, imageNormal)
        isNew = False
    else:
        cv2.imwrite(previousImage, imageNormal)
        isNew = True

    #check if file exists.
    canCompare = os.path.isfile(previousImage)

    #proceed with the comparison.
    if(canCompare):
        
        print 'Compare start...'

        model = cv.LoadImage(modelImage)
        
        fgbg = cv2.BackgroundSubtractorMOG()
        print 'fgbg'
        fgmask = fgbg.apply(model)
        print 'fgmask'
        cv2.imwrite('images\Zexperimental.jpg', fgmask)
        print 'done...'
        
        print 'Compare end...'
        
    
    key = cv2.waitKey(4000)
    if key == 113:
        print 'Close camera (q)'
        break
    elif key == 27:
        print 'Close camera (esc)'        
        break
    
cv2.destroyAllWindows()
