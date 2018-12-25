while True:
    try:
        m = float(input())
        mensagem = ''
        m *= 86400
        hora = m/3600
        m = float(m % 3600)
        minuto = m/60
        m = int(m % 60)
        print(hora, minuto, m)

    except EOFError:
        break
