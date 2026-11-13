from ipaddress import ip_network

for ip in ip_network('172.21.198.77/255.255.240.0', strict=False):
    print(ip)
    break

print(172+21+192+0)
# 385