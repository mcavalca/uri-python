f = [0, 1]
for i in range(2,42):
    f.append(f[i-1]+f[i-2])
f.pop(0)

while True:
    n = int(input())
    if n == 0:
        break
    print(f[n])