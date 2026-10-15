from functools import cache

@cache
def f(x):
    if x == 68:
        return 1
    if x > 68:
        return 0
    if x > 64:
        return 0
    return f(x+1) + f(x+3) + f(x*2)

print(f(10))

# 6184