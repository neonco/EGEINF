with open('24.txt') as file:
    s = file.readline()

s = s + 'ZZ'

t = []
for l, c, r in zip(s, s[1:], s[2:]):
    if l != r:
        t += [l]
    else:
        t += [l, c, ' ']

t = ''.join(t)
s = t.split()
s = [x for x in s if x.count('D') >= 2]
print(s[:2])
s = [x.rfind('D') - x.find('D') + 1 for x in s if x.count('D') >= 2]
print(s[:2])

print(max(s))

# 433