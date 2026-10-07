file = open('23_32111.txt').readlines()

m = [x.split() for x in file]
m = [(int(s), int(e), float(w)) for s, e, w in m]


k = [float('inf')]*1001
i = 1
k[i] = 0
print(k)

for s, e, w in m:
    if s == i:
        k[e] = k[s] + w

print(k)
# дорешать с Дэшками 10
