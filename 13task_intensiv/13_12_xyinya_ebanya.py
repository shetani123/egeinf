from ipaddress import *

for mask in range(1,33):
    net = ip_network(f'111.233.75.16/{mask}', 0)
    print(net, net.netmask)