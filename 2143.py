while True:
    n = int(input())
    if not n:
        break
    pessoas = []
    while n:
        n -= 1
        x = int(input())
        if x % 2 == 0:
            pessoas.append((2 * x) - 2)
        else:
            pessoas.append((2 * x) - 1)
    for i in pessoas:
        print(i)        
