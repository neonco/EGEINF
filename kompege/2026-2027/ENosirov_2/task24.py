with open('24_32194.txt') as file:
    s = file.readline()

print(set(s))
print(len(s))

a = []
for i, symbol in enumerate(s):
    if symbol == 'A':
        a.append(i)

m = []
for left, start, end, right in zip(a, a[1:], a[100:], a[101:]):
    t = s[left+1: right]
    q = s[start+1: end]
    # print(t.count('A'), q.count('A'))
    # print(t.count('B'), q.count('B'))
    if q.count('B') <= 80 and len(t) > 530:
        m.append(t)


print(len(m))

res = 0
for ind, subs in enumerate(m):
    print(ind)
    for i in range(0, len(subs)-1):
        for j in range(i+100, len(subs)):
            t = subs[i:j+1]
            if t.count('A') == 100:
                if t.count('B') <= 80:
                    res = max(res, len(t))

print(res)
# дорешать


