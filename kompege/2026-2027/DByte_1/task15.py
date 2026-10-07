p = range(15, 30+1)
q = range(60, 80+1)

pairs = []
for i in range(-100, 300):
    for j in range(i+1, 300):
        pairs += [(i, j)]

res = 0
for start, end in pairs:
    a = range(start, end+1)
    for x in range(-200, 400):
        c = not((x not in a) or (x in p))
        b = not((x not in a) or (x not in q))
        if (not c or b) == 0:
            break
    else:
        # print(end-start, start, end)
        res = max(res, end-start)

print(res)

# 20