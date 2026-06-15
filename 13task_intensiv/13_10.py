from ipaddress import *
k = 0
for mask in range(1,33):
    net = ip_network(f'142.198.113.106/{mask}', 0)
    print(net, net.netmask)

b = bin(255)[2:] + bin(255)[2:] + bin(254)[2:]
print(b.count('1'))
#20 21 22 23