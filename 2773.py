from math import sqrt

while True:
    try:
        xi, yi, xf, yf, v = [int(x) for x in input().split()]
        xl, yl, xr, yr = [int(x) for x in input().split()]
        ximenor = min(abs(xi - xl), abs(xi - xr))
        yimenor = min(abs(yi - yl), abs(yi - yr))
        xfmenor = min(abs(xf - xl), abs(xf - xr))
        yfmenor = min(abs(yf - yl), abs(yf - yr))
        print(ximenor, yimenor)
        print(xfmenor, yfmenor)

    except EOFError:
        break
