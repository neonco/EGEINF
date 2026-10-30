def f(a, b, t, h=0):
    flag = h % 2 == t % 2
    if a + b >= 167:
        return flag
    if h > t:
        return False
    m = [
        f(a+5, b, t, h+1),
        f(a, b+5, t, h+1),
        f(a*3, b, t, h+1),
        f(a, b*3, t, h+1),
    ]

    return all(m) if flag else any(m)

for s in range(1, 154+1):
    for t in range(20):
        if f(12, s, t):
            print(s, t)
            break

# 19   18
# 20   17 42
# 21   44