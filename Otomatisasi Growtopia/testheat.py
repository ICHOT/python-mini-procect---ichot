import pyautogui as pg
import time
from location import *
time.sleep(1)
a = 0
pg.moveTo(Egg)
pg.leftClick()
while a < len_oven:
    print("Add Flour", a+1)
    pg.moveTo(locate[a])
    pg.leftClick()
    pg.moveTo(Low)
    time.sleep(0.8)
    pg.leftClick()
    time.sleep(0.8)
    a += 1
