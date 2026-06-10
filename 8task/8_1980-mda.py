from itertools import *

k = 0

for i in product("ABCWXYZ", repeat = 6):
    s = ''.join(i)
    if (s[0] == "W" or s[0] == "X" or s[0] == "Y" or s[0] == "Z") and (
            s[-1] == "W" or s[-1] == "X" or s[-1] == "Y" or s[-1] == "Z"):
        if "W" not in s[2:-1] and "X" not in s[2:-1] and "Y" not in s[2:-1] and "Z" not in s[2:-1]:
            k += 1
print(k)