from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

res = (f(2042) + 7*f(2041)) // f(2040)
print(res)

# 4182009