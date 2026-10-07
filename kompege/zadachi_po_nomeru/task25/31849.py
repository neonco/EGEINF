from math import prod

primes = []
for n in range(1, 100_000):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            break
    else:
        if '3' in str(n) and '5' in str(n):
            primes.append(n)

# print(len(primes))

n = 4_300_000
for x in range(n+1, n+1_000_000):
    c = []
    temp = x
    for p in primes:
        while x % p == 0:
            c.append(p)
            x //= p
    if len(c) == 3 and prod(c) == temp:
        print(temp, c, prod(c))

# 4300579 1531
# 4334287 1543
# 4362377 1553
# 4446647 1583
# 4924177 1753