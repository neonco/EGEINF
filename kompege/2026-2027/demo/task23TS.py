# написано ассистентом (opencode), пользователь будет переписывать
from graphlib import TopologicalSorter

edges = {}
with open('23_31518.txt') as file:
    for row in file:
        a, b, w = row.split()
        a, b, w = int(a), int(b), float(w)
        edges.setdefault(a, []).append((b, w))

ts = TopologicalSorter()
for u, outs in edges.items():
    for v, _ in outs:
        ts.add(v, u)

dist = {1: 0}
for u in ts.static_order():
    if u not in dist:
        continue
    for v, w in edges.get(u, []):
        nd = dist[u] + w
        if nd < dist.get(v, float('inf')):
            dist[v] = nd

print(int(dist[100]))
