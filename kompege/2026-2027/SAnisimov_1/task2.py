for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not (z == w) and not y and (x or z)
                if f == 1:
                    print(z, x, w, y, f)

# zxwy
