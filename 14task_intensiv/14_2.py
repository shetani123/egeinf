n = 17 * 16**455 + 2**67 - 4**47 + 58
n8 = ''
k = 0
while n > 0:
    n8 = str(n % 8) + n8
    n //= 8
for i in n8:
    if i == '0' or i == '2' or i == '4':
        k += 1
print(k)