from collections import Counter

with open('24.txt') as f:
    s = f.readline().strip()

# s = 'SQRP RPSQRPSQRPSR PSQRPSQRPSQ SQRPSQRPSQR'

print(Counter(s))
print(s[:200])
s = s.replace('SQRP', 'AAAA')

s = s.replace('ASQR', 'AAAA ')
s = s.replace('ASQ', 'AAA ')
s = s.replace('AS', 'AA ')

s = s.replace('QRPA', ' AAAA')
s = s.replace('RPA', ' AAA')
s = s.replace('PA', ' AA')

for x in 'SQRP':
    s = s.replace(x, ' ')

s = s.split()
s = [len(x) for x in s]
# print(s[:200])
print(max(s))

# 52


