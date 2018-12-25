from collections import Counter
while True:
    try:
        palavra = input()
        letras = Counter(palavra)
        total = 0
        for i in palavra:
            print(i, letras[i])
            if (letras[i] % 2 == 1):
                total += 1
        print(total)

    except EOFError:
        break
