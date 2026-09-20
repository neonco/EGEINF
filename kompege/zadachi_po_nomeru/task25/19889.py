# задача 19889

def f(n):
    m = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            m.append(d)
            m.append(n // d)
    m = set(m)
    return sorted(m)


for n in range(902714+1, 902714+50):
    dels = f(n)
    dels = [x for x in dels if x % 10 == 5 and x != 5 and x != n]
    if dels:
        print(n, dels)
