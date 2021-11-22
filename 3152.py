def res(x,y):
   n=len(x)
   area=0
   j=n-1
   for i in range(n):
      area+=(x[j]+x[i])*(y[j]-y[i])
      j=i
   return area/2
x1=[]
x2=[]
y1=[]
y2=[]
for uno in range(4):
   s=list(map(int,input().split()))
   x1.append(s[0])
   y1.append(s[1])
for dos in range(4):
   s=list(map(int,input().split()))
   x2.append(s[0])
   y2.append(s[1])
print("terreno ",end="")
print("B") if (abs(res(x2, y2)) >= abs(res(x1, y1))) else print("A")
