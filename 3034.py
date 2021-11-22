def primo(n):
    if n < 2:return False
    if n%2==0:return False
    k=3
    while k*k<=n:
         if n%k==0:return False
         k+=2
    return True
for _ in range(int(input())):
    n=int(input())+1
    if n<7:print("No")
    elif n%7==0 and n%2!=0 and primo(n+2):print("Yes")
    else:print("No")
