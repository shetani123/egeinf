from ipaddress import *

net = ip_network('211.46.0.0/255.255.128.0',0)
k = 0
for i in net:
    b = f'{i:b}'
    if b.count('1') % 4 == 0 and b[-2:] == '11':
        k += 1
print(k)
