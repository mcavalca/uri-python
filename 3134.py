def v(a,b,c,d):
    if a+b==c+d:return True
    elif a+c==d+b:return True
    elif a+d==b+c:return True
    elif a==b+c+d:return True
    elif b==c+d+a:return True
    elif c==a+b+d:return True
    elif d==a+b+c:return True
    return False
a=int(input().replace('.',''))
b=int(input().replace('.',''))
c=int(input().replace('.',''))
d=int(input().replace('.',''))
print("YES") if v(a,b,c,d) else print("NO")
