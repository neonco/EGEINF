for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x or y) == (not y or z)) and (y or w)
                if f == 1:
                    print(x, z, w, y, f)

# xzwy