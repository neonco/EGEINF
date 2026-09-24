with open('task17.txt') as f:
    m = [int(x) for x in f.readlines()]

lim = max([x for x in m if len(str(abs(x))) == 4 and abs(x) % 100 == 23])
# lim = max([x for x in m if len(str(abs(x))) == 4 and str(abs(x))[-2:] == '23'])
# lim = max([x for x in m if 1000 <= abs(x) <= 9999 and abs(x) % 100 == 23])
# 9523


def f(n):
    if len(str(abs(n))) == 4 and abs(n) % 10 == 1:
            return True
    return False


res = []
for trio in zip(m, m[1:], m[2:]):
    if sum(trio) > lim:
       if sum((f(x) for x in trio)) == 2:
           res.append(sum(trio))

print(len(res), max(res))

# 29 89829
