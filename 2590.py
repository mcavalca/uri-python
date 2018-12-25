t = int(input())
while t > 0:
    t -= 1
    n = int(input()) % 4
    if n == 0:
        print(1)
    elif n == 1:
        print(7)
    elif n == 2:
        print(9)
    elif n == 3:
        print(3)
