# from sys import setrecursionlimit
# setrecursionlimit(50_000)


def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if '1' in str(x):
        return f(x+1, end) + f(int(str(x).replace('1', '3')), end)
    else:
        return f(x+1, end)


res = f(11, 94)

print(res)

# 832