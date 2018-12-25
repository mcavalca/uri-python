from math import sqrt
quad = [0] * 11001
for i in range(int(sqrt(11000)) + 1):
    for j in range(i, int(sqrt(11000)) + 1):
        if(i * i + j * j) > 11000:
            break
        quad[i*i + j*j] = 1

while True:
    try:
        n = int(input())
        if n < 0:
            print('NO')
        else:
            if quad[n]:
                print('YES')
            else:
                print('NO')

    except EOFError:
        break
