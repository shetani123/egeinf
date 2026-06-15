from ipaddress import *

net = ip_network('192.168.12.207/255.192.0.0',0)
for i in range(-1,-1000,-1):
    ip = net[i]
    b = f'{ip:b}'
    if b.count('1') == b.count('0'):
        print(ip)