notas = [2, 5, 10, 20, 50, 100]
while True:
    n, m = input().split()
    if(n == '0' and m == '0'):
        break
    n = int(n)
    m = int(m)
    m -= n
    total = 0
    
    for i in notas:
        if(m == i*2):
            print('possible')
            total = 2
            break
            
    if total == 0:
        for i in range(len(notas)-1, -1, -1):
            if total == 3:
                break
            if m - notas[i] >= 0:
                m -= notas[i]
                total += 1
        if (m == 0 and total == 2):
            print('possible')
        else:
            print('impossible')
    