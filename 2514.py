from math import gcd
while True:
    try:
        m = int(input())
        l = [int(x) for x in input().split()]
        mmc = l[0]
        for i in l[1:]:
            mmc = ( (mmc * i) // (gcd(mmc, i)) )
        mmc -= m
        print(mmc)

    except EOFError:
        break
