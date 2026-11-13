def f(a, b, t, h=0):
    flag = t % 2 == h % 2
    if a + b >= 150:
        return flag
    if h > t:
        return False
    m = [
        f(a+4, b, t, h+1),
        f(a, b+4, t, h+1),
        f(a*2, b, t, h+1),
        f(a, b*2, t, h+1),
    ]
    return all(m) if flag else any(m)


for s in range(1, 128+1):
    for t in range(8):
        if f(21, s, t):
            print(s, t)
            break

# 19  33
# 20  32, 52
# 21  48