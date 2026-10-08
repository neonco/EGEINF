from ipaddress import ip_network

net = ip_network('192.168.159.86/255.255.252.0', False)
for ip in net:
    print(ip)
    break

print(192+168+156+0)
# 516