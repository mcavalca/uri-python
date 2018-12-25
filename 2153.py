while True:
    try:
        palavra = input()
        rev = palavra[len(palavra)-1::-1]
        j = 1
        for i in range(1 , int(len(rev)/2)):
            print('PALAVRAS = ', rev[:i], rev[i:i+j])
            if (rev[:i] == rev[i:i+j]):
                rev = rev[i:]
                break
            j += 1
        palavra = rev[len(rev)-1::-1]
        print(palavra)

    except EOFError:
        break
