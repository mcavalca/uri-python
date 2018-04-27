num = 0
while True:
    num += 1
    try:
        n = int(input())
        p = []
        inst = []
        k = -1
        p = list(map(int, input().split()))
        inst.append(0)
        if(inst[0] == int(p[0])):
            k = 0
        else:
            for i in range(1, n):
                inst.append(int(p[i-1])+inst[i-1])
                if((inst[i] == int(p[i])) and (k == -1)):
                    k = int(p[i])
        print("Instancia", num)
        if(k != -1):
            print(k)
        else:
            print("nao achei")
        print()
        p.clear()
        inst.clear()
            
        
    except EOFError:
        break