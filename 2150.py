while True:
    try:
        vogal = input()
        frase = input()
        total = 0
        for letra in vogal:
            total += frase.count(letra)
        print(total)

    except EOFError:
        break
