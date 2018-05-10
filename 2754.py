from decimal import Decimal

i = 234.345
j = 45.698

print('%.6f - %.6f'%(i, j))
print('%.0f - %.0f'%(i, j))
print('%.1f - %.1f'%(i, j))
print('%.2f - %.2f'%(i, j))
print('%.3f - %.3f'%(i, j))
print('%.6e - %.6e' % (Decimal(i), Decimal(j)))
print('%.6E - %.6E' % (Decimal(i), Decimal(j)))
print('%g - %g'%(i, j))
print('%g - %g'%(i, j))