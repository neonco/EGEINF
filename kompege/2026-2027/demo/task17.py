from itertools import pairwise

# 1 считать файл
with open('17_31514.txt') as file:
    m = [int(s) for s in file.readlines()]

# 2 найти якорное число из задачи
limit = min(m)

# 3 пройтись по всему массиву и сравнить с якорем

# село, но работает
for i in range(len(m)-1):
    a, b = m[i], m[i+1]
    print(a, b)

# город-сказка
for a, b in zip(m, m[1:]):
    print(a, b)

# для гениев, но не универсальный

res = []
for a, b in pairwise(m):
    # if a % 33 == limit or b % 33 == limit:
    if limit in (a % 33, b % 33):
        res += [a + b]

print(len(res), max(res))

# 622 174933
