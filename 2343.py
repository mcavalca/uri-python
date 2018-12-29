n = int(input())
raio = 0
i = 502
quad = [[0] * i for x in range(i)]

while n:
    n -= 1
    x, y = [int(i) for i in input().split()]
    if not raio:
        if quad[int(x)][int(y)] == 0:
            quad[int(x)][int(y)] = 1
        else:
            raio = 1

print(raio)
