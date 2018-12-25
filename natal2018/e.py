e, d = [int(x) for x in input().split()]
if d < e:
    print('Eu odeio a professora!')
elif d - e >= 3:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    if e + 2 < 24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')
