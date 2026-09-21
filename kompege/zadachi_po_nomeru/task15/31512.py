b = range(70, 90 + 1)

for a in range(1, 3000):
    for x in range(1, 5000):
        f = (x % a == 0) or (x not in b) or (x % 22 != 0)
        if not f:
            break
    else:
        print(a)

# 88