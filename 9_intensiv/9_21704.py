for s in open('9_21704.csv'):
    a = list(map(int, s.split()))
    if a[0] > a[1] > a[2] > a[3] > a[4] > a[5] > a[6]:
        if (a[0]+a[6])/2 > (a[1]+a[2]+a[3]+a[4]+a[5])/5:
            print(sum(a))
            break