from itertools import *

k = 0

for i in product("САЛО" , repeat = 6):
    s = ''.join(i)
    if 1 <= s.count("О") <= 3:
        k += 1
print(k)