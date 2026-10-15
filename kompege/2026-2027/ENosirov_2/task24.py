with open('24_32194.txt') as file:
    s = file.readline()

print(set(s))
print(len(s))

ind_a = []
for i, symbol in enumerate(s):
    if symbol == 'A':
        ind_a.append(i)

res = []
for start, end in zip(ind_a, ind_a[101:]):
    t = s[start: end+1]
    if len(t) > 500:
        res.append((len(t), t.count('B'), t.count('A'), t))

res = sorted(res, reverse=True)
for x in res:
    print(x)
    break

# дорешать


