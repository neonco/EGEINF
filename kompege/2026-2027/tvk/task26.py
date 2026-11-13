with open('26_32510.txt') as f:
    k, n = [int(x) for x in f.readline().split()]
    m = [y.split() for y in f.readlines()]
    m = [[int(a), int(b), c, int(d)] for a, b, c, d in m]




s = sum(d for a, b, c, d in m)
m = sorted(m)

print(k, n, len(m), s)

okno = [0]*(k+1)
ves  = [0]*(k+1)

count = 0
last = 0
for start, end, tip, konfeti in m:
    for i in range(1, len(okno)):
        if tip == 'V':
            if i % 2 == 1:
                if start >= okno[i]:
                    okno[i] = end + 14
                    ves[i] += konfeti
                    count += 1
                    last = i
                    break
        if tip == 'P':
            if i % 2 == 0:
                if start >= okno[i]:
                    okno[i] = end + 14
                    ves[i] += konfeti
                    count += 1
                    last = i
                    break

print()
print(count, ves[last])
print(sum(ves))

# 8459 9682