import cv2
import numpy as np

winname = "GRS"
bgs_mog = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture(2)

if __name__ == "__main__":
    while capture.isOpened():
        _,frame = capture.read()
        fgmask = bgs_mog.apply(frame)
        #mask_rbg = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)
        #draw = frame & mask_rbg
        
        cv2.imshow(winname, fgmask)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cv2.destroyAllWindows()
