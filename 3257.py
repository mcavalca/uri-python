def res(x):
   a=[]
   i=1
   for c in x:
      a.append(c+i)
      i+=1
   return a
n=int(input())
x=list(map(int,input().split()))
x.sort(reverse=True)
a=res(x)
print(max(a)+1)
