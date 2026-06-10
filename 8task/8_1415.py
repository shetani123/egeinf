from itertools import *

k = 0

for i in product("AA123", repeat = 8):
    s = "".join(i)
    if s.count("A") == 2:
        k += 1
        print(s)
print(k)