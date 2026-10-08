from ipaddress import ip_network

net = ip_network('145.92.137.200/28', False)
for ip in net:
    print(ip)
    break
print(net.netmask)

# 255 + 248
print(255+240)

# 495