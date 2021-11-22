from math import factorial as fat
def primo(n):
    if n < 2:return False
    if n==2:return True
    if n%2==0:return False
    k=3
    while k*k<=n:
         if n%k==0:return False
         k+=2
    return True
n=int(input())
x=list(map(int,input().split()))
for i in x:
    if primo(i):print(f"{i}! = {fat(i)}")
