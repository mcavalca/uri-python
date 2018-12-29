x = int(input())
partic = {}
while x:
    x -= 1
    entrada = input().split()
    partic[entrada[0]] = [entrada[1], entrada[2], entrada[3]]

while True:
    try:
        pessoa, presente = input().split()
        if pessoa in partic:
            if presente in partic[pessoa]:
                print('Uhul! Seu amigo secreto vai adorar o/')
            else:
                print('Tente Novamente!')
        else:
            print('Tente Novamente!')

    except EOFError:
        break
