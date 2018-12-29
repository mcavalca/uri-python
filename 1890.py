t = int(input())
while t:
    t -= 1
    c, d = [int(x) for x in input().split()]
    placas = (26**c) * (10**d)
    if placas == 1:
        placas = 0
    print(placas)
