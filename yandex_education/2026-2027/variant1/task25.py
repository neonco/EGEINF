def is_prime(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    else:
        return True

def factor(n):
    res = []
    for d in range(1, int(n**0.5)+1): # боль
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))


print(is_prime(31))
print(factor(100))

# если число представимо как квадрат простого числа, то оно имеет 3 делителя:
# n = p**2 => n делится на 1, p, p**2. в таком случае нетривиальнызх простых делителей будет ровно 1,
# а значит разность максимального и минимального будет 0 (p - p)

start = 3_300_000
for number in range(start+1, start+2000):
    divs = factor(number)
    divs = [d for d in divs if is_prime(d)]
    m = divs[-1] - divs[1]
    if str(m) == str(m)[::-1] and m % 10 == 5:
        # print(number, divs, m)
        print(number, m)

# 3300440 575
# 3300598 545
# 3300858 5555
# 3301288 585
# 3301692 545