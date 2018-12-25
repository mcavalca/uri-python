while True:
    try:
        k, n = input().split()
        n = int(n)
        temp = [0] * len(k)
        while n > 0:
            for x in range(9,-1, -1):
                for y in range(len(k)):
                    if k[y] == str(x):
                        temp[y] = 1
                        n -= 1
                    if n < 1:
                        break
                if n < 1:
                    break
        menor = ''
        for x in range(len(temp)):
            if temp[x] == 0:
                menor += str(k[x])
        print(menor)

    except EOFError:
        break
