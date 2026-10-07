from ipaddress import ip_network

for ip in ip_network('192.168.76.35/22', False):
    print(ip)

print(255 + 255 + 255 - 2 - 1)

# 762