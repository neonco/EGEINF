for n in range(21, 100):
    o = oct(n)[2:]
    if n % 7 == 0:
        o = o + o[-2:]
    else:
        o = oct((n % 7) * 7)[2:] + o
    r = int(o, base=8)
    print(n, o, r)

# 57 771 505