distancia = 0
check = 0
v_ant = 0
while True:
    try:
        tempo = input().split(':')
        # if len(tempo[2]) > 2:
        try:
            tempo[2], v = tempo[2].split(' ')

        except:
            pass

        if check:
            tempo_ant = h + m + s

        h, m, s= [float(x) for x in tempo]
        m /= 60
        s /= 3600
        tempo_fin = h + m + s

        if check:
            tempo_fin -= tempo_ant
            distancia += float(v) * tempo_fin
            print('%s:%s:%s %.2f km' % (tempo[0], tempo[1], tempo[2], distancia))


        check = 1

    except EOFError:
        break
