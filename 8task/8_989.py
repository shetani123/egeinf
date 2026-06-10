from itertools import *

k = 0

for i in product("АИМРЯ", repeat = 4):
    s = "".join(i)
    k += 1
    if k == 211:
        print(s)
        break
