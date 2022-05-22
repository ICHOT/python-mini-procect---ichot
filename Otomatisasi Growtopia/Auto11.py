import pyautogui as pg
import time
from location import *
time.sleep(1)

# sw = 175, 263
# pw = 240, 263
# pg.moveTo(sw)
# pg.doubleClick()
a = 0
pg.moveTo(Flour)
pg.doubleClick()
while a < len_oven11:
    print("Add Flour", a+1)
    pg.moveTo(locate11[a])
    pg.doubleClick()
    time.sleep(1)
    pg.moveTo(Low)
    pg.doubleClick()
    time.sleep(1)
    a += 1

b = 0
pg.moveTo(Egg)
pg.doubleClick()
while b < len_oven11:
    print("Add Egg", b+1)
    pg.moveTo(locate11[b])
    pg.doubleClick()
    time.sleep(0.1)
    b += 1

c = 0
pg.moveTo(Milk)
pg.doubleClick()
# time.sleep(2)
# pg.moveTo(pw)
# pg.doubleClick()
while c < len_oven11:
    print("Add Milk", c+1)
    pg.moveTo(locate11[c])
    pg.doubleClick()
    time.sleep(0.1)
    c += 1

d = 0
pg.moveTo(Berry)
pg.doubleClick()
time.sleep(10)
# pg.moveTo(pw)
# pg.doubleClick()
while d < len_oven11:
    print("Add Berry", d+1)
    pg.moveTo(locate11[d])
    pg.doubleClick()
    time.sleep(0.1)
    d += 1

e = 0
print("Wait...")
pg.moveTo(Hand)
pg.doubleClick()
time.sleep(17)
# pg.moveTo(pw)
# pg.doubleClick()
while e < len_oven11:
    print("Collect Oven ", e+1)
    pg.moveTo(locate11[e])
    pg.doubleClick()
    time.sleep(0.1)
    e += 1
# pg.moveTo(sw)
# pg.doubleClick()
print("Coocking Finish..")
