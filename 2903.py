r = float(input())
i = 1
if 360 % (i * r) != 0:
    while (i * r) % 360 != 0:
        i += 1
else:
    i = int(360/r)

print(i)
