from sys import setrecursionlimit
setrecursionlimit(3000)

# проще решить руками, в репо есть решение
# тут увеличение глубины рекурсии работает, потому что ...

def f(n):
    if n == 1:
        return 1
    return (n+1) * f(n-1)  # ... только 1 вызов функции внутри


a = (f(2025) // 2026)
b = (a + f(2024))
c = b // f(2023)

print(c)

# 4050