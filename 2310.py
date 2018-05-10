n = int(input())
t = [0, 0, 0]
s = [0, 0, 0]
while n > 0:
    n -= 1
    c = input()
    for i in range(1):
        l = [int(x) for x in input().split()]
        for x in range(3):
            t[x] += l[x]
        l = [int(x) for x in input().split()]
        for x in range(3):
            s[x] += l[x]
    
print('Pontos de Saque: %.2f %%.' % (100*(s[0]/t[0])))
print('Pontos de Bloqueio: %.2f %%.' % (100*(s[1]/t[1])))
print('Pontos de Ataque: %.2f %%.' % (100*(s[2]/t[2])))