maior = 0
ant = 0

while True:
    try:
        n = int(input())
        if ant > n and maior == 0:
            maior = ant + 1
        ant = n
        
    except EOFError:
        break
        
if maior == 0:
    maior = ant + 1
print(maior)