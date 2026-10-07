def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n // d]
    return sorted(set(res))


k = 1_103_285_717
for n in range(k, k + 1000000):
    divs = f(n)
    if len(divs) == 3:
        if str(divs[1]).count('16') == 1:
            print(n, divs[1])
    if len(divs) == 4:
        if divs[2] % divs[1] != 0:
            if str(divs[1]).count('16') == 1:
                if str(divs[2]).count('16') == 1:
                    print(n, divs[1])



