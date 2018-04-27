n = int(input())

while(n):
    i = int(input())
    i = 2015 - i
    if(i < 1):
        i = abs(i-1)
        print(i,"A.C.")
    else:
        print(i,"D.C.")
    n -= 1