t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    c = [int(x) for x in input().split()]
    print(len(set(c)))