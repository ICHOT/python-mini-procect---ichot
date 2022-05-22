import pyautogui as pg
import time

print("Wait 5 sec")
time.sleep(5)

# print(pg.position())
print("Memasukan Tepung Ke Stove")
pg.moveTo(509, 659)
pg.leftClick()
time.sleep(1)
pg.moveTo(581, 195)
pg.leftClick()
time.sleep(1)

print("Suhu Api Low Heat")
# pg.moveTo(300, 427)
pg.moveTo(357, 427)
pg.leftClick()
time.sleep(2)

print("Memasukan Egg Ke Stove")
pg.moveTo(803, 561)
pg.leftClick()
time.sleep(1)
pg.moveTo(581, 195)
pg.leftClick()
time.sleep(1)

print("Memesukan Milk Ke Stove")
pg.moveTo(308, 658)
pg.leftClick()
time.sleep(1)
# 7 sec
pg.moveTo(581, 195)
time.sleep(19)
pg.leftClick()
time.sleep(1)


print("Memesukan B Beery Ke Stove")
pg.moveTo(506, 561)
pg.leftClick()
time.sleep(1)
pg.moveTo(581, 195)
time.sleep(10)
pg.leftClick()
time.sleep(1)

print("Menunggu Masakan Matang")
pg.moveTo(300, 555)
pg.leftClick()
time.sleep(1)
pg.moveTo(581, 195)
time.sleep(19)
pg.leftClick()
print("Makanan Sudah Matang Siap Di Angkat")
time.sleep(1)
