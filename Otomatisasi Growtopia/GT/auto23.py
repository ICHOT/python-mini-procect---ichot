import pyautogui as pg
import time
from location import *


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time: = {0}:{1}:{2}".format(int(hours), int(mins), sec))


time.sleep(1)
start_time = time.time()
b = 0
pg.moveTo(Egg)
pg.leftClick()
while b < len_oven:
    print("Add Egg", b+1)
    pg.moveTo(locate[b])
    pg.leftClick()
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    time.sleep(0.4)
    b += 1

c = 0
pg.moveTo(Milk)
pg.leftClick()
time.sleep(14.1)

while c < len_oven:
    print("Add Milk", c+1)
    pg.moveTo(locate[c])
    pg.leftClick()
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    time.sleep(0.4)
    c += 1

d = 0
pg.moveTo(Berry)
pg.leftClick()
time.sleep(1)

while d < len_oven:
    print("Add Berry", d+1)
    pg.moveTo(locate[d])
    pg.leftClick()
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    time.sleep(0.4)
    d += 1

e = 0
print("Wait...")
pg.moveTo(Hand)
pg.leftClick()
time.sleep(8.3)

while e < len_oven:
    print("Collect Oven ", e+1)
    pg.moveTo(locate[e])
    pg.leftClick()
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    time.sleep(0.4)
    e += 1

print("Coocking Finish..")
