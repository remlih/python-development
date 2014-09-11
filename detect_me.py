#import the modules
import time
import SimpleCV
from SimpleCV import Image
from SimpleCV import Color

hay_alguien = Image("me.jpg")

win = hay_alguien.show()
time.sleep(3)
win.quit()

extraccion_color = hay_alguien.colorDistance(Color.BLACK)
win = extraccion_color.show()
time.sleep(3)
win.quit()

me = hay_alguien - extraccion_color
win = me.show()
time.sleep(3)
win.quit()

print('resultados primera comparacion:')
R = me.meanColor()[2]
print('R: ' + str(R))
G = me.meanColor()[1]
print('G: ' + str(G))
B = me.meanColor()[0]
print('B: ' + str(B))

cam = SimpleCV.Camera()
mylaptopcam = SimpleCV.Camera(1, prop_set = {"width": 1280, "height": 720})
alternativa = mylaptopcam.getImage()

#alternativa = Image("me.jpg")

extraccion_color = alternativa.colorDistance(Color.BLACK)
win = extraccion_color.show()
time.sleep(3)
win.quit()

me = alternativa - extraccion_color
print('resultados segunda comparacion:')
R = me.meanColor()[2]
print('R: ' + str(R))
G = me.meanColor()[1]
print('G: ' + str(G))
B = me.meanColor()[0]
print('B: ' + str(B))

if (G < 5):
    print('Aqui estoy!!')
else:
    print('No estoy!!')

