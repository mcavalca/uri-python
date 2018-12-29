while True:
    try:
        numero = input().upper()
        # numero = (' '.join(numero)).upper()
        saida = ''
        listanumeros = '0123456789*#'
        for digito in numero:
            if digito in listanumeros:
                saida += digito
            elif digito == 'A' or digito == 'B' or digito == 'C':
                saida += '2'
            elif digito == 'D' or digito == 'E' or digito == 'F':
                saida += '3'
            elif digito == 'G' or digito == 'H' or digito == 'I':
                saida += '4'
            elif digito == 'J' or digito == 'K' or digito == 'L':
                saida += '5'
            elif digito == 'M' or digito == 'N' or digito == 'O':
                saida += '6'
            elif digito == 'P' or digito == 'Q' or digito == 'R' or digito == 'S':
                saida += '7'
            elif digito == 'T' or digito == 'U' or digito == 'V':
                saida += '8'
            elif digito == 'X' or digito == 'Y' or digito == 'W' or digito == 'Z':
                saida += '9'


        print(saida)

    except EOFError:
        break
