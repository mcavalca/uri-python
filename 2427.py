l = float(input())
n = 1
i = 1
while l >= 2.0:
    print(l)
    l /= 2
    n += i
    i += 1

print(2**n)
