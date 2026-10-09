l = 5_800_000
l1 = 5_800_000 / 100 / 100
l2 = 5_800_000 / 999 / 999

primes = []
for n in range(2, int(l1)):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            break
    else:
        primes.append(n)

print(primes)
for n in range(l, l-3000, -1):
    for p in primes:
        if n % p == 0:
            t = n // p
            if int(t**0.5) == t**0.5:
                # print(t**0.5, t, p, t * p, n)
                print(n, p)
                break

# 5799600 179
# 5799536 431
# 5799421 181
# 5799104 251
# 5797952 17