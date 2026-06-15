from ipaddress import *

net = ip_network('136.36.240.16/255.255.255.248')
k = 0
for i in net:
    b = f'{i:b}'
    if '101' not in b:
        k+=1
print(k)