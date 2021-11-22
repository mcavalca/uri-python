def pretobranco(n,tot):
    if n%2==0:return tot//2,tot//2
    return (tot+1)//2,((tot+1)//2)-1

n=int(input())
b,p=pretobranco(n,n*n)
print(f"{b} casas brancas e {p} casas pretas")
