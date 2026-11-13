def f(a, b, t, h=0):
    flag = t % 2 == h % 2
    if a + b >= 131:
        return flag
    if h > t:
        return False
    m = [
        f(a+1, b, t, h+1),
        f(a, b+1, t, h+1),
        f(a*2, b, t, h+1),
        f(a, b*2, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(1, 117+1):
    for t in range(8):
        if f(13, s, t):
            print(s, t)
            break

# 19   116 (это надо просто смотреть глазами)
# 20   52 58
# 21   51 (в ответ 1)