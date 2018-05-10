while True:
    n, k = input().split()
    if n == '0' and k == '0':
        break
    p = [int(i) for i in input().split()]
    total = 0
    for i in set(p):
        if p.count(i) >= int(k):
            total += 1
    print(total)