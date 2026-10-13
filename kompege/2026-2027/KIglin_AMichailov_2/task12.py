# машина тьюринга

print(bin(2027))
print(f'{2027:b}')

m = [
    [[],         [],        [2, -1, 1],],
    [[0, -1, 1], [0, 0, 1], [1, -1, 2],],
    [[],         [],        [2, 0, 2],],
]

s = '222222' + f'{2027:b}' + '222222'
print(s)
s = list(s)
i = 17
q = 0
while True:
    row = m[q]
    print(row)
    col = int(s[i])
    cell = row[col]
    s[i] = str(cell[0])
    if cell[1] == 0:
        break
    i += cell[1]
    q = cell[2]

print(''.join(s))

