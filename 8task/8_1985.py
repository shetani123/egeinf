from itertools import *

k = 0

for i in permutations("АБИКОЛУН", 8):
    s = ''.join(i)
    s.replace("И", "А").replace("О","А").replace("У","А")
    s.replace("К","Б").replace("Л","Б").replace("Н","Б")
    if "АА" not in s and "ББ" not in s:
        k += 1
print(k)