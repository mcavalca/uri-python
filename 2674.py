from math import sqrt

def primo(n):
    if (n == 2):
        return 1
    if (n == 0 or n == 1 or (n % 2 == 0)):
        return 0
    for i in range(3, int(sqrt(n)) + 2):
        if (n % i == 0):
            return 0
    return 1

def super(n):
    while n >= 10:
        s = n % 10
        n = int(n / 10)
        if not primo(s):
            return 0
    if(n == 2 or n == 3 or n == 5 or n == 7):
        return 1
    else:
        return 0

while True:
    try:
        n = int(input())
        if not primo(n):
            print('Nada')
        else:
            if super(n):
                print('Super')
            else:
                print('Primo')

    except EOFError:
        break
