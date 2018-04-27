while(True):
    m, n = input().split()
    if(m == '0' and n == '0'):
        break
    m = int(m) + int(n)
    val = int(str(m).replace('0',''))
    print(val)