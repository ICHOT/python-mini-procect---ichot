import random
from seedPharse import *

pharse_write = open("seedPharse.txt", "w")
pharse_read = open("seedPharse.txt", "r")

count = 1
counts = 0
list = pharse_read.readlines()
while count <= 200000:
    a = random.randint(0, lengh_seed)
    b = random.randint(0, lengh_seed)
    c = random.randint(0, lengh_seed)
    d = random.randint(0, lengh_seed)
    e = random.randint(0, lengh_seed)
    f = random.randint(0, lengh_seed)
    g = random.randint(0, lengh_seed)
    h = random.randint(0, lengh_seed)
    i = random.randint(0, lengh_seed)
    j = random.randint(0, lengh_seed)
    k = random.randint(0, lengh_seed)
    l = random.randint(0, lengh_seed)
    if a == seed[599] and b == seed[1226] and c == seed[1449] and d == seed[1176] and e == seed[154] and f == seed[1003] and g == seed[672] and h == seed[1073] and i == seed[1834] and j == seed[590] and k == seed[1327] and l == seed[1103]:
        print(seed[599])
        print(seed[1226])
        print(seed[1449])
        print(seed[1176])
        print(seed[154])
        print(seed[1003])
        print(seed[672])
        print(seed[1073])
        print(seed[1834])
        print(seed[590])
        print(seed[1327])
        print(seed[1103])
        break
    else:
        print(f"===={counts}====")
        count += 1
        counts += 1
