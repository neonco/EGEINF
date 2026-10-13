# print(int('30041', 6) + 1)

from itertools import product

word = sorted('СОЛНЦЕ')
# print(word)

i = 0
for x in product(word, repeat=6):
    i += 1
    if i % 2 != 0 and x[0] not in 'НЦ' and x.count('Ц') == 1 and x.count('Н') == 1:
        print(i, x)

# 38619 ('С', 'Ц', 'С', 'С', 'С', 'Н')
