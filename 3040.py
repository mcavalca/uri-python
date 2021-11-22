def x(h,d,g):
   if h>=200 and h<=300 and d>=50 and g>=150:return True
   return False
for i in range(int(input())):
   h,d,g=map(int,input().split())
   print("Sim") if x(h,d,g) else print("Nao")
