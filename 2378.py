n, c = [int(x) for x in input().split()]
pessoas = 0
exc = 0

while n:
    n -= 1
    s, e = [int(x) for x in input().split()]
    pessoas += e
    pessoas -= s
    if pessoas > c:
        exc = 1

if exc:
    print('S')
else:
    print('N')
