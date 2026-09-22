for a in range(1, 10_000):
    for x in range(1, 100_000):
        f = not (x % 33 == 0) or (not (x % a != 0) or (x % 242 != 0))
        if f == 0:
            break
    else:
        print(a)

# 726
