# здесь решение плохое, но рабочее. иногда необходимо поступиться принципами, даже в такой простой задаче на 2 указателя в 2-ух массивах

with open("26.txt") as f:
    n, d = [int(x) for x in f.readline().split()]
    m = [row.split() for row in f.readlines()]
s = [[int(num), 1] for num, type in m if type == 'S']
g = [[int(num), 1] for num, type in m if type == 'G']

s = sorted(s)[::-1]
g = sorted(g)[::-1]
print(s[:5], g[:5], len(s), len(g))
count = 0
res = 0
# for i in range(len(s)):
#     if i % 1000 == 0:
#         print(i)
#     for j in range(len(g)):
#         if abs(g[j][0] - s[i][0]) <= d  and g[j][1] == 1:
#             s[i][1] = g[j][1] = 0
#             count += 1
#             if count == 1:
#                 res = max(s[i][0], g[j][0])
#             break
            
print(count, res)

print(s[:10])
print(g[:10])

# 30414 999999
