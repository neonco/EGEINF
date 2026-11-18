for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (z or not w) or ((not y or not w) and (z or x))
                if f == 0:
                    print(y, x, w, z)

                    # yxwz