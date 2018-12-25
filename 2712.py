n = int(input())
while n:
    n -= 1
    placa = input().split('-')
    if (len(placa) == 2) and (len(placa[0]) == 3) and (len(placa[1]) == 4) and (placa[0] == placa[0].upper()):
        try:
            check = int(placa[1])
            r = int(placa[1][3])
            if r > 8 or r == 0:
                print('FRIDAY')
            elif r > 6:
                print('THURSDAY')
            elif r > 4:
                print('WEDNESDAY')
            elif r > 2:
                print('TUESDAY')
            else:
                print('MONDAY')
        except:
            print('FAILURE')
    else:
        print('FAILURE')
