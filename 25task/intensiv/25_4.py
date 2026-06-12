from fnmatch import fnmatch

for x in range(0,10**7,159):
    if fnmatch(str(x), '2?1*67'):
        print(x, x//159)