import math

while True:
    l, c, r1, r2 = input().split()
    r1 = int(r1) + int(r1)
    r2 = int(r2) + int(r2)
    l = int(l)
    c = int(c)
    d1 = ((r1/2)*math.sqrt(2) - r1/2)/2
    d2 = ((r2/2)*math.sqrt(2) - r2/2)/2
    if(l == 0 and c == 0 and r1 == 0 and r2 == 0):
        break
    hip = math.sqrt(l**2+c**2) - d1 - d2
    # print(r1, r2, l, c, hip, d1, d2)
    if r1 + r2 <= l:
        print('S')
    #    print('CASO 1')
    elif r1 + r2 <= c:
        print('S')
    #    print('CASO 2')
    elif r1 + r2 <= hip:
        print('S')
    #    print('CASO 3')
    else:
        print('N')