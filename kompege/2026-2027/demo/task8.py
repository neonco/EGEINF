# print(int('30041', 6) + 1)

from itertools import product

word = sorted('АКЦЕНТ')
print(word)

i = 0
for x in product(word, repeat=5):
    i += 1
    if i % 2 == 0 and x[0] not in 'АЕК' and 'Т' in x:
        print(i, x)

# 3914 ('Н', 'А', 'А', 'Т', 'Е')
