def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    elif x % 10 > (x % 100) // 10:
        z = str(x)
        z = int(z[0]+z[2]+z[1])
        return f(x+1, end) + f(z, end)
    else:
        return f(x+1, end)


print(f(112, 165))

# 89