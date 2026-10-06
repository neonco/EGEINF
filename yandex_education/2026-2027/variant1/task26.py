with open('26.txt') as f:
    m = f.readlines()

n, budget = [int(x) for x in m[0].split()]
m = [row.split() for row in m[1:]]
m = [(int(price), worker) for price, worker in m]
m = sorted(m)
# print(n, budget, m[:2]

s = 0
gap = 0
work = {'D':0, 'G':0}
for i, (price, worker) in enumerate(m):
    if s + price <= budget:
        work[worker] += 1
        s += price
        gap = budget - s
    else:
        break

left = [p for p, w in m[:i] if w == 'D'][::-1]
right = [p for p, w in m[i:] if w == 'G']

print(s, gap, work, i)

for l, r in zip(left, right):
    diff = r - l
    if gap - diff >= 0:
        gap -= diff
        work['G'] += 1
        work['D'] -= 1
    else:
        break

print(gap, work)

# 186 9
