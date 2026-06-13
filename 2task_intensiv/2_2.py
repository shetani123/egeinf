for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x <= y) and (y <= z) and (z <= w)
                if f == True:
                    print(w, x, y, z, f)

