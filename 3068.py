t=1
while True:
    x1,y1,x2,y2=map(int,input().split())
    if x1==y1==x2==y2==0:break
    met=0
    n=int(input())
    while n>0:
        m1,m2=map(int,input().split())
        if m1>=x1 and m1<=x2:
            if m2<=y1 and m2>=y2:met+=1
        n-=1
    print(f"Teste {t}\n{met}")
    t+=1
