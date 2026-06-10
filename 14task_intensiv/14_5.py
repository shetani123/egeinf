n = 2**2045 + 2**1800 - 2**1000 + 4**700 - 2024
n8 = []
while n > 0:
    n8.append(n%8)
    n //= 8
print(sum(n8))