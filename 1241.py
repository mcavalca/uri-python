n = int(input())

while(n > 0):
    n -= 1
    a, b = input().split()
    if(len(a) < len(b)):
        print('nao encaixa')
    else:
        if(a[len(a)-len(b)::] == b):
            print('encaixa')
        else:
            print('nao encaixa')