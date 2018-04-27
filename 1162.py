import math

def merge(l, s):
    meio = len(l)//2
    esqu = l[:meio]
    dire = l[meio:]
    
    if(len(esqu)>1):
        s = merge(esqu, s)
    if(len(dire)>1):
        s = merge(dire, s)
        
    i = 0
    j = 0
    k = 0
    
    while i < len(esqu) and j < len(dire):
        if esqu[i] < dire[j]:
            l[k] = esqu[i]
            i += 1
        else:
            l[k] = dire[j]
            j += 1
            s += abs(j-i) + 1
        k += 1
    
    while i < len(esqu):
        l[k] = esqu[i]
        i += 1
        k += 1
        
    while j < len(dire):
        l[k] = dire[j]
        j += 1
        k += 1
        
    return s

n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    train = input().split()
    for i in range(m):
        train[i] = int(train[i])
    swap = 0
    swap = merge(train, swap)
    print('Optimal train swapping takes %d swaps.' % swap)