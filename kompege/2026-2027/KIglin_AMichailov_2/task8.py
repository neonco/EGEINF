from itertools import product

i = 0
for x in product(sorted('АЛГОСЫ'), repeat=5):
    i += 1
    if i % 2 == 1:
        if x[0] not in 'АГ' and x.count('Ы') >= 2:
            print(i, x)

# 2803 ('Л', 'А', 'Ы', 'Ы', 'А')