for n in range(1, 20):
    b = bin(n)[2:]

    s = sum(int(digit) for digit in b)
    if s % 2 == 0:
        b = b + '00'
    else:
        b = '11' + b[1:] + '1'

    r = int(b, base=2)
    print(n, b, r)

# 19
