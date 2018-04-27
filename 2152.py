n = int(input())
while(n > 0):
    n -= 1
    h, m, o = input().split()
    r = ''
    if((int(h) < 10) and (len(h) == 1)):
        r = '0' + h
    else:
        r = h
    r += ':'
    if((int(m) < 10) and (len(m) == 1)):
        r += '0' + m
    else:
        r += m
    r += ' - A porta '
    if(o == '0'):
        r += 'fechou!'
    else:
        r += 'abriu!'
    print(r)