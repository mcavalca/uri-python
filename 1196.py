keyb = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
while True:
    try:
        frase = input()
        decod = ''
        for c in frase:
            if c == ' ':
                decod += c
            else:
                decod += keyb[keyb.index(c)-1]
        print(decod)
    except EOFError:
        break