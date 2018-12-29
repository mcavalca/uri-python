while True:
    a, b, c, x, y = [int(i) for i in input().split()]
    if a == b == c == x == y == 0:
        break
    p1 = sorted([a, b, c])
    p2 = sorted([x, y])
    print(p1, p2)
