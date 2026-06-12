def f(x):
    return ((a1 <= x <= a2) and not(35 <= x <= 48)) <= ((15 <= x <= 33) or (35 <= x <= 48))

maxi = 0
for a1 in range(1,1000):
    for a2 in range(a1,1000):
        if all(f(x) for x in range(1,10**5)):
            if maxi < a2-a1:
                maxi = a2-a1
print(maxi)