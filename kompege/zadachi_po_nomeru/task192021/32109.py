def f(s, t, h=0):
    flag = h % 2 == t % 2
    if s >= 100:
        return flag
    if h > t:
        return False
    m = [
        f(s+2, t, h+1),
        f(s+4, t, h+1),
        f(s*2, t, h+1),
    ]
    return all(m) if flag else any(m)


for s in range(1, 99+1):
    for t in range(9):
        if f(s, t):
            print(s, t)
            break


# 19  48
# 20  24 44
# 21  42