import math
pi = 3.1415
r, l = input().split()
r = float(r)
volume = ((4.0*pi*r*r*r)/3.0)
print(math.floor(float(l)/volume))
