d = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

i = 0
for x in range(3):
    j = r[x] - d[x]
    if j > 0:
        i += j

print(i)