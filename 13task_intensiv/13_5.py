from ipaddress import *

net = ip_network('10.22.44.0/255.255.252.0',0)
k=0

for i in net:
    b = f'{i:b}'
    if b.count('1') % 2 == 0:
        k+=1
print(k-2)