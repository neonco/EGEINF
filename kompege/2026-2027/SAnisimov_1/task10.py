from ipaddress import ip_network

net = ip_network("148.92.138.52/255.255.192.0", strict=False)

res = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 3 == 0:
        print(ip, b)
        res += 1

print(res)
# 5462