import math
c = int(input())

while(c > 0):
    c -= 1
    n, m = input().split()
    print(math.ceil(float(n)/float(m)))