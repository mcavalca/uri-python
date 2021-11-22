for i in range(int(input())):
    x=list(map(int,input().split()))
    z=x.pop(0)
    print(sum(x)-z+1)
