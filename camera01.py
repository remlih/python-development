#import the modules
import SimpleCV
import time

def takePhoto():
    try:
        cam = SimpleCV.Camera()
        mylaptopcam = SimpleCV.Camera(2, prop_set = {"width": 1280, "height": 720})
        d = mylaptopcam.getImage()
        #d = d.crop(180,150,350,350)
        d.save("me_t.jpg")
        win = d.show()
        time.sleep(3)
        print('listo!!')
    except Exception as ex:
        print('Unhandled error: ' , ex)
    finally:
        time.sleep(2)
        win.quit()
        del cam

takePhoto()
