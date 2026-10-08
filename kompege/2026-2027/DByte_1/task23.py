file = open('23_32111.txt').readlines()

m = [x.split() for x in file]
m = [[int(s), int(e), float(w)] for s, e, w in m]
# удаляем все дуги где 825 либо начало, либо конец
m = [[s, e, w] for s, e, w in m if 825 not in (s, e)]

# не удаляем дуги, но делаем их бесконечными, алгоритм теряет к ним интерес
# m = [[s, e, float('inf')] if 825 in (s, e) else [s, e, w] for s, e, w in m]

k = [float('inf')] * 1001
cur_vertex = 1
k[cur_vertex] = 0
ban = []

for _ in range(1002): # с избытком, но кого волнует?
    for s,e,w in m:
        if s == cur_vertex:
            k[e] = min(k[e], k[s] + w)
    ban += [cur_vertex]

    min_s = float('inf')
    for i, s in enumerate(k):
        if s < min_s and i not in ban:
            min_s = s
            cur_vertex = i

print(k[100])

# 11782