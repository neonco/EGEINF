with open('24.txt') as f:
    s = f.readline()

s = '_' + s + '_'
m = []
for i, x in enumerate(s):
    if x in '@_':
        m.append([i, x])

res = []
for a, b, c, d in zip(m, m[1:], m[2:], m[3:]):
    if b[0] - a[0] > 1 and c[0] - b[0] > 1 and d[0] - c[0] > 1:
        if b[1] + c[1] == '@_':
            t = s[a[0]+1:d[0]]
            res.append(t)

ans = max(res, key=len)
print(ans, len(ans))
# profimatikaurnnvihczltszajtvptagjmwyykqclrxheqynofxwnmhenrjyehprovkuozlstjnjqcvpicdfjspjjlnekatpfmajupashoztyukgxqvgqwdmnteddijrrnxgcql_xfxtdzswxvojtxufwzfyenxiwniuhh
# 166

