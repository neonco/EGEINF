from fnmatch import fnmatch

mask = '7?2*4??9?'
gap = 10**10
for n in range(0, gap, 96437):
    if fnmatch(str(n), mask):
        print(n, n // 96437)

# 7322943595 75935
# 7325547394 75962
# 7723542893 80089
# 7726146692 80116
# 7823644499 81127
# 7826248298 81154
