from ipaddress import *

for mask in range(1,33):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    print(net,net.netmask)