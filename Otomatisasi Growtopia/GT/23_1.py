from ctypes import cdll
import pyautogui as pg
import time
from location import *

time.sleep(1)
# start_time = time.time()


# def time_convert(sec):
#     mins = sec // 60
#     sec = sec % 60
#     hours = mins // 60
#     mins = mins % 60
#     print("Time: = {0}:{1}:{2}".format(int(hours), int(mins), sec))


b = 0
c = 0
d = 0
e = 0


def loop_oven(a, text, recipe, time_sleep):
    pg.moveTo(recipe)
    pg.leftClick()
    time.sleep(time_sleep)
    while(a) < len_oven:
        print(text, a+1)
        pg.moveTo(locate[a])
        pg.leftClick()
        # end_time = time.time()
        # time_lapsed = end_time - start_time
        # time_convert(time_lapsed)
        time.sleep(0.4)
        a += 1


loop_oven(b, "Add Egg", Egg, 0)
loop_oven(c, "Add Milk", Milk, 14.1)
loop_oven(d, "Add Berry", Berry, 1)
loop_oven(e, "Collect Oven", Hand, 8.3)
