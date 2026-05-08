from fnmatch import *
for x in range(0,10**13, 206):
    if fnmatch(str(x), '12?345?67089?'):
        print(x, x // 206)