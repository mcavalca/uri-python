def r10(n):
    if n == 0:
        return 6
    x = 6+1/r10(n-1)
    return x

n = int(input())
x = r10(n)-3
print('%.10f' % x)