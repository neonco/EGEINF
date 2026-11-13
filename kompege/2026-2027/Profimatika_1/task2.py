from itertools import product

for w, x, y, z in product(range(2), repeat=4):
    f = ((x == y) or not(not z or x)) or not w
    if f == 0:
        print(z, w, x, y)

# zwxy
