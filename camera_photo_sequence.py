import time
import cv2.cv as cv2


winName = 'Image display'
cameraIndex = 0

capture = cv2.CaptureFromCAM(cameraIndex)

def takePhoto():
    global winName
    global cameraIndex    
    try:        
        if capture:
            cv2.NamedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
            frame = cv2.QueryFrame(capture)
            return frame
    except Exception as ex:
        print('Unhandled error: ', ex)

def startSequence(frame):
    print 'start sequence...'
    i = 1
    while (i <= 5):
        print 'Save image'
        cv2.SaveImage('test1.jpg', frame)
        time.sleep(3)
        i = i + 1

if __name__ == "__main__":
    while True:
        frame = takePhoto()
        cv2.ShowImage(winName, frame)

        key = cv2.WaitKey(30)

        if key == ord(' '):
            startSequence(frame)
##          print 'Save image'
##          cv2.SaveImage('test1.jpg', frame)
        elif key == ord('q'):
            print 'Close camera (q)'
            break
        elif key == 27:
            print 'Close camera (esc)'
            break  
        
    cv2.DestroyWindow(winName)     
    
