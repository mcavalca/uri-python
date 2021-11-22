d,p=map(int,input().split())
aux=1
for i in range(1,p):aux*=(d-i)/d
aux=(1-aux)*100
print("%.2f"%aux)
