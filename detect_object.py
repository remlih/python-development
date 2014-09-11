#import the modules
import time
from SimpleCV import Image
from SimpleCV import Color

car_in_lot = Image("parking-car.png")
car_not_in_lot = Image("parking-no-car.png")

car = car_in_lot.crop(470,200,200,200)
win = car.show()
time.sleep(1)
win.quit()

yellow_car = car.colorDistance(Color.YELLOW)
win = yellow_car.show()
time.sleep(1)
win.quit()

only_car = car - yellow_car
win = only_car.show()
time.sleep(1)
win.quit()

print('resultados primera comparacion:')
R = only_car.meanColor()[2]
print('R: ' + str(R))
G = only_car.meanColor()[1]
print('G: ' + str(G))
B = only_car.meanColor()[0]
print('B: ' + str(B))

car_not_in_lot = Image("parking-no-car.png")
no_car = car_not_in_lot.crop(470,200,200,200)

yellow_car = no_car.colorDistance(Color.YELLOW)
win = yellow_car.show()
time.sleep(1)
win.quit()

only_car = car - yellow_car
print('resultados segunda comparacion:')
R = only_car.meanColor()[2]
print('R: ' + str(R))
G = only_car.meanColor()[1]
print('G: ' + str(G))
B = only_car.meanColor()[0]
print('B: ' + str(B))

if (R > 15 and G > 10):
    print('Car is in the lot!!')
else:
    print('Car is not in the lot!!')
