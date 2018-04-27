import math

while(True):
    a = input()
    acm = 0
    if(a == '0'):
        break
    a = a[::-1]
    for i, j in enumerate(a):
        acm += int(j) * int(math.factorial(i+1)) 
    print(acm)