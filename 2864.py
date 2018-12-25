n = int(input())
while n > 0:
    n -= 1
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    x = - ( b / ( 2 * a ) )
    y = a*x*x + b*x + c
    print("%.2f" % y)
