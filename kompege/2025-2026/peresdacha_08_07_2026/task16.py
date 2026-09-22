from sys import setrecursionlimit
setrecursionlimit(50_000)

def f(n):
    if n == 1:
        return 1
    return (n + 1) * f(n - 1)


res = (f(42_038) + 3 * f(42_037)) / f(42_036)

print(res)

# 1767361596