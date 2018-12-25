from datetime import date
d0 = input().split()
d1 = input().split()
d0 = date(2007, int(d0[1]), int(d0[0]))
d1 = date(2007, int(d1[1]), int(d1[0]))
dif = d1 - d0
print(dif.days)
