b = 0
a = 0
m = 0
d = 0
for i in range(int(input())):
    e,g,h = input().split()
    h=int(h)
  
    if(g=='bonecos'):
        b = b + h
    elif(g=='arquitetos'):
        a = a + h
    elif(g=='musicos'):
        m = m + h
    elif(g=='desenhistas'):
        d = d + h
a = int(a/4)
b = int(b/8)
d = int(d/12)
m = int(m/6)
total = a+b+d+m

print(total)
