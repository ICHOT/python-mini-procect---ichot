from operator import le
import pyautogui as pg
import time
from location import *
time.sleep(1)
sw = 175, 263
pw = 240, 263
pg.moveTo(sw)
pg.leftClick()

a = 0
pg.moveTo(Flour)
# pg.leftClick()
while a < len_oven:
    print("Add Flour", a+1)
    pg.moveTo(locate[a])
    # pg.leftClick()
    time.sleep(1)
    pg.moveTo(Low)
    # pg.leftClick()
    time.sleep(1)
    a += 1


b = 0
pg.moveTo(Egg)
# pg.leftClick()
while b < len_oven:
    print("Add Egg", b+1)
    pg.moveTo(locate[b])
    # pg.leftClick()
    time.sleep(0.1)
    b += 1


c = 0
pg.moveTo(Milk)
# pg.leftClick()
time.sleep(2)
pg.moveTo(pw)
pg.leftClick()
while c < len_oven:
    print("Add Milk", c+1)
    pg.moveTo(locate[c])
    # pg.leftClick()
    time.sleep(0.1)
    c += 1


d = 0
pg.moveTo(Berry)
time.sleep(7.8)
pg.moveTo(pw)
pg.leftClick()
# pg.leftClick()
while d < len_oven:
    print("Add Berry", d+1)
    pg.moveTo(locate[d])
    # pg.leftClick()
    time.sleep(0.1)
    d += 1


e = 0
print("Wait...")
pg.moveTo(Hand)
time.sleep(14.5)
pg.moveTo(pw)
pg.leftClick()
# pg.leftClick()
while e < len_oven:
    print("Collect Oven ", e+1)
    pg.moveTo(locate[e])
    # pg.leftClick()
    time.sleep(0.1)
    e += 1
pg.moveTo(sw)
pg.leftClick()
print("Coocking Finish..")
