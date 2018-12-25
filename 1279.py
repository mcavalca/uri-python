pula = 0
while True:
    try:
        ano = int(input())
        b = 0
        ord = 1
        if pula:
            print('')
        pula = 1

        if (ano % 4 == 0) and (not (ano % 100 == 0) or (ano % 400 == 0)):
            print('This is leap year.')
            b = 1
            ord = 0
        if (ano % 15 == 0):
            print('This is huluculu festival year.')
            ord = 0
        if (ano % 55 == 0) and b:
            print('This is bulukulu festival year.')

        if ord:
            print('This is an ordinary year.')


    except EOFError:
        break
