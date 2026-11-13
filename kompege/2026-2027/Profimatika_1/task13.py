def f(n, end):
    if n == end:
        return 1
    if n > end:
        return 0
    a, b = (n // 10) % 10, n % 10
    if a < b:
        return f(n + 1, end) + f(n + 9*(b - a), end)
    return f(n + 1, end)


print(f(100, 152))

