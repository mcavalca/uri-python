from decimal import Decimal
a = input()
if Decimal(a) >= 0 and a[0] != '-':
    print('+', end='')
    
print('%.4E' % Decimal(a))