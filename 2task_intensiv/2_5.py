print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = w and ((x <= y) == (y <= z))
                if f == True:
                    print(x,y,z,w,f)
