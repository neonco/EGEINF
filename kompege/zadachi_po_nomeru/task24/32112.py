from string import ascii_uppercase

with open('24_32112.txt') as f:
    s = f.readline().strip()

print(len(s))
print(set(s))
for sym in ascii_uppercase:
    s = s.replace(sym, ' ')

s = s.split()
print(max(s, key=len))
#

# s = ['1111111222223']
res = 0
for row in s:
    for l in range(0, len(row)-1):
        for r in range(l+1, len(row)):
            t = row[l:r+1]
            if len(set(t)) <= 3:
                res = max(res, len(t))

print(res)

# 14

# s_double_pointer = sum([len(x)*2 for x in s])
# s_dummy = sum([len(x)*len(x)//2 for x in s])
# print(s_double_pointer, s_dummy)
# двойной указатель в этой задаче не шибко лучше чем просто тупой перебор
# не будь Андреем (олимпиадное_движение), делай проще

