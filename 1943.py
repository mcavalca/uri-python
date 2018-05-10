n = int(input())
print('Top ', end = '')
if n <= 1:
    print('1')
elif n <= 3:
    print('3')
elif n <= 5:
    print('5')
elif n <= 10:
    print('10')
elif n <= 25:
    print('25')
elif n <= 50:
    print('50')
elif n <= 100:
    print('100')