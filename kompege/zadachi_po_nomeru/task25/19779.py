# задача 19779
# ищем все делители числа, среди них — оканчивающиеся на 777, проверяем делитель на простоту

def f(n):
    m = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            m.append(d)
            m.append(n // d)
    m = set(m)
    return sorted(m)


for n in range(55_000_000+1, 55_000_000+5_000_000):
    d = f(n)
    d = [x for x in d if x % 1000 == 777]
    d = [x for x in d if len(f(x)) == 2]
    if d:
        print(n, d)
