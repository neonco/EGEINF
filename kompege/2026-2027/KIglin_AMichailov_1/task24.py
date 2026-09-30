from collections import Counter

with open('24.txt') as f:
    s = f.readline()

# print(Counter(s))
print(len(s))
# print(s[:100])

save = s

alph = set(s)
for b in alph:
    if b not in '0123456789ABCDEF':
        s = s.replace(b, ' ')

s = s.split()
s = sorted(s, key=len, reverse=True)
l = [len(x) for x in s]
print(s[:5])
print(l[:5])

print(save.index(s[0])+1)  # если у самой длиной подстроки убрать первый ноль

# 8551770