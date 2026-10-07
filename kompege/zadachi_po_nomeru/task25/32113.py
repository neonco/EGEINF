def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

start = 500_000
for n in range(start+1, start+20):
    divs = [d for d in f(n) if d % 10 == 3]
    divs = [d for d in divs if d not in (3, n)]
    if divs:
        print(n, divs[0])

# 500002 53
# 500004 43
# 500006 13
# 500010 7143
# 500011 4673