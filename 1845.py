maior = 'BJPSVXZ'
menor = 'bjpsvxz'

while True:
    try:
        c = input()
        efit = ''
        for i in range(len(c)):
            if c[i] in maior:
                efit += 'F'
            elif c[i] in menor:
                efit += 'f'
            else:
                efit += c[i]
        print(efit)
        
    except EOFError:
        break