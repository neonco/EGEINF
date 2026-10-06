with open('23_31518.txt') as file:
    m = file.readlines()

m = [row.split() for row in m]
print(m[0])
m = [[int(s), int(e), float(w)] for s, e, w in m]
print(m[0])

g = [float('inf')] * 1001
ind = 1
g[ind] = 0
prev = []

while len(prev) < 1000:
    for s, e, w in m:
        if s == ind:
            g[e] = min(g[e], g[s] + w)
    prev.append(ind)
    ind = min([(s, i) for i, s in enumerate(g) if i not in prev])[1]

print(int(g[100]))

# 10971