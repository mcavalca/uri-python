for _ in range(int(input())):
    j=m=0
    for joao in range(3):
        x=list(map(int,input().split()))
        j+=(x[0]*x[1])
    for maria in range(3):
        x=list(map(int,input().split()))
        m+=(x[0]*x[1])
    print("MARIA") if m>j else print("JOAO")
