n = '1'
m = '1'

while(True):
    n, m = input().split()
    # print(n,m)
    if(n == '0' and m =='0'):
        break
    
    while (len(n) > 1):
        n0 = 0
        for i in n:
            n0 += int(i)
        n = str(n0)
        
    while (len(m) > 1):
        m0 = 0
        for i in m:
            m0 += int(i)
        m = str(m0)
    
    if(int(n) == int(m)):
        print(0)
    elif(int(n) > int(m)):
        print(1)
    elif(int(n) < int(m)):
        print(2)