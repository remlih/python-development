import cv2
import numpy as np

winname = "GRS"
bgs_mog = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture(2)
x, y, h, w = (493, 305, 125, 90)

if __name__ == "__main__":
    while capture.isOpened():
        _,frame = capture.read()
        fgmask = bgs_mog.apply(frame)
##        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

##        template = cv2.imread('post-it2.jpg',0)
##        w, h = template.shape[::-1]
##        res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
##        threshold = 0.8
##        loc = np.where( res >= threshold)
##        for pt in zip(*loc[::-1]):
##            cv2.rectangle(fgmask, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
##        cv2.rectangle(fgmask,(x,y),(x+w,y+h),(255,0,0),2)        
        cv2.imshow(winname, fgmask)
        
        key = cv2.waitKey(1)
        if key == 113:
            print 'Close camera (q)'
            break
        elif key == 27:
            print 'Close camera (esc)'        
            break
    
    cv2.destroyAllWindows()

