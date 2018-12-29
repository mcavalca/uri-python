t = int(input())
while t:
    t -= 1
    i = input()
    qt = bin(int(i)).count('1')
    print(qt)
