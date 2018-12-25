from datetime import datetime, timedelta
while True:
    try:
        m, d = input().split()
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        data = '2016' + m + d
        natal = '20161225'
        data = datetime.strptime(data, '%Y%m%d')
        natal = datetime.strptime(natal, '%Y%m%d')
        dias = (natal - data).days
        if dias == 0:
            print('E natal!')
        elif dias == 1:
            print('E vespera de natal!')
        elif dias < 0:
            print('Ja passou!')
        else:
            print('Faltam %d dias para o natal!' % dias)

    except EOFError:
        break
