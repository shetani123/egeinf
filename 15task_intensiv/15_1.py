def f(x):
    return (17 <= x <= 58) <= (((29 <= x <= 80) and not(a1 <= x <= a2)) <= (not(17 <= x <= 58)))

min1 = 11000000
for a1 in range(1,100):
    for a2 in range(a1, 150):
        if all(f(x) for x in range(1, 10**5)):
            if min1 > a2-a1:
                min1 = a2-a1
print(min1)