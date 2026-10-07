from collections import defaultdict

graph = defaultdict(set)

with open('23_31846.txt') as f:
    m = [x.split() for x in f.readlines()]

for start, end, weight in m:
    graph[start].add(end)



# дорешать
