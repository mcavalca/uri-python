n = int(input())
while n > 0:
    n -= 1
    l = bin(int(input()))
    l = l[2:]
    m = 0
    aux = 0
    for i in l:
        if i == '1':
            aux += 1
        else:
            aux = 0
        if aux > m:
            m = aux
            
    print(m)