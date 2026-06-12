a = [int(x) for x in open("17_6024.txt")]

k = 0

m = max([x**2 for x in a if str(x)[-1] == "2" and str(x)[-2] == "1"])

maxi = 0

for i in range(len(a)-1):
    if (str(a[i])[-1] == "2" and str(a[i])[-2] == "1") or (str(a[i+1])[-1] == "2" and str(a[i+1])[-2] == "1"):
        if (a[i] + a[i+1])**2 < m:
            k += 1
            if maxi < a[i] + a[i+1]:
                maxi = a[i] + a[i+1]
print(k, maxi)