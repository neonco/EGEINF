def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [n % d, n // d]
    return sorted(set(res))

n = 1

for x in range(n + 1, n + 1000000):
    d = f(x)
    if len(d) == 4:
        a, b = d[1], d[2]
        if len(f(a)) == 2 and len(f(b)) == 2:
            print(d)