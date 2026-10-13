with open("24.txt") as f:
    s = f.readline()

rtv = []
for i in range(len(s)-2):
    if s[i:i+3] == 'RTV':
        rtv.append(i)

s = s.replace('RTV', 'XXX')

t = []
for i in range(len(s)):
    if s[i] == 'T':
        t.append(i)

# дорешать с 11 классом
