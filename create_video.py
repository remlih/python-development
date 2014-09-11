import cv2

img1 = cv2.imread('images\Zmodel.jpg')
img2 = cv2.imread('images\Zmodel.jpg')
img3 = cv2.imread('images\Zmodel.jpg')

height , width , layers =  img1.shape

video = cv2.VideoWriter('images\video.avi',-1,1,(width,height))

video.write(img1)
video.write(img2)
video.write(img3)

print 'done!!'

cv2.destroyAllWindows()
#video.release()


#
# NOT WORK.
#
