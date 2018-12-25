a, b = [int(x) for x in input().split()]
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print(q, r)
