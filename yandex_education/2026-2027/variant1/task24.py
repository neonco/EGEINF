from collections import Counter

with open('24.txt') as file:
    s = file.readline().strip()

# print(Counter(s))

s = s.replace('Z', 'Z ').split()
s = [x[::-1] for x in s]
res = []
for seq in s:
    sum_digits = 0
    count_vowel = 0
    for i, symbol in enumerate(seq):
        if symbol in 'AIOUE':
            count_vowel += 1
        # if symbol.isdigit():
        if symbol in '0123456789':
            sum_digits += int(symbol)
        if count_vowel == 50:
            if symbol == 'A' and sum_digits % 7 == 0:
                res.append(seq[:i+1])
                break

res = [len(seq) for seq in res]
print(max(res))

# 707