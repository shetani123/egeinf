from itertools import *

k = 0

for i in product('КРЕСЛО', repeat = 4):
    s = ''.join(i)
    if (s[0] == 'К' or s[0] == 'Р' or s[0] == "С" or s[0] == "Л") and (s[-1] == "О" or s[-1] == "Е"):
        k += 1
print(k)