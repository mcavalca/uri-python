for i in range(int(input())):
   a,b,c,d=map(int,input().split())
   print("S") if (a<c and b<d) or (b<c and a<d) else print("N")
