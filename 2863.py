while True:
    try:
        n = int(input())
        tempo = 100.0
        while n > 0:
            t = float(input())
            if t < tempo:
                tempo = t
            n -= 1
        print(tempo)

    except EOFError:
        break
