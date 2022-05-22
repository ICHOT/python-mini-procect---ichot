import random
import threading
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
    if a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and a != j and a != k and a != l and b != c and b != d and b != e and b != f and b != g and b != h and b != i and b != j and b != k and b != l and c != d and c != e and c != f and c != g and c != h and c != i and c != j and c != k and c != l and d != e and d != f and d != g and d != h and d != i and d != j and d != k and d != l and e != f and e != g and e != h and e != i and e != j and e != k and e != l and f != g and f != h and f != i and f != j and f != k and f != l and g != h and g != i and g != j and g != k and g != l and h != i and h != j and h != k and h != l and i != j and i != k and i != l and j != k and j != l and k != l:
        pharse_write.write(
            f"==={count}==={counts} \n{seed[a]} {seed[b]} {seed[c]} {seed[d]} {seed[e]} {seed[f]} {seed[g]} {seed[h]} {seed[i]} {seed[j]} {seed[k]} {seed[l]}\n\n")
        count += 1
        counts += 1

    else:
        # print(f"==={count}==={counts}\nPass")
        # print(
        #     f"==={count}=== \n{seed[a]} {seed[b]} {seed[c]} {seed[d]} {seed[e]} {seed[f]} {seed[g]} {seed[h]} {seed[i]} {seed[j]} {seed[k]} {seed[l]}\n\n")
        counts += 1
print("total work : ", counts)
# print(threading.activeCount())
