while True:
    try:
        l = []
        n, m = input().split()
        l = [int(x) for x in input().split()]
        total = sum(l[int(n)-int(m):])
        print(total)
        
        
    except EOFError:
        break