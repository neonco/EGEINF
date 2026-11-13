def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n // d]
    return sorted(set(res))

k = 4_501_347_296
primes = []
for n in range(1, int(k**0.5)+1):
    if len(f(n)) == 2:
        if str(n).count('53') == 1:
            primes.append(n)
print(len(primes))

res = []
for n in range(k+1, k+100_000):
    for p in primes:
        if n % p == 0:
            if len(f(n // p)) == 2:
                if str(n // p).count('53') == 1:
                    print(n, p, n // p)

# 4501351109 53
# 4501367009 53
# 4501371143 53
# 4501382209 50153
# 4501382909 53