from itertools import permutations
while True:
    try:
        letras = input()
        possiveis = [''.join(p) for p in permutations(letras)]
        print(possiveis)
    except EOFError:
        break
