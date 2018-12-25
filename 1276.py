import string

while True:
    try:
        palavra = sorted(set(input()))
        alfabeto = string.ascii_lowercase
        faixa = []
        for letra in palavra:
            print()
        print(alfabeto)
        print(palavra)


    except EOFError:
        break
