a = int(input())
b = int(input())
c = int(input())

print('A = %d, B = %d, C = %d' % (a, b, c))
print('A = %10.0d, B = %10d, C = %10d' % (a, b, c))
print('A = %s, B = %10d, C = %10d' % (str(a).zfill(10), b, c))
print('A = {:<10}, B = {:<10}, C = {:<10}'.format(a, b, c))
