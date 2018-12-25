c = int(input())
while c:
    c -= 1
    n, m = [int(x) for x in input().split()]
    n = str(n ** m)
    print(n)
    print(len(n))
