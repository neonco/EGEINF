from collections import Counter

with open('24_31905_31905.txt') as f:
    s = f.readline().strip()

print(Counter(s))
print(s[:50])
for x in ['++', '**', '+*', '*+']:
    s = s.replace(x, '  ')

for x in [' +', ' *', '+ ', '* ']:
    s = s.replace(x, '  ')

for y in '02457':
    for x in ['+0', '*0']:
        s = s.replace(x+y, x+' '+y)

s = s.split()
s = [x for x in s if '*' in x and '+' in x]
s = sorted(s, key=len, reverse=True)
s = [(x, len(x)) for x in s]
print(s[:2])

# первое длины 130 надо убрать только первый ноль
# второе длины 127
# ответ 129

