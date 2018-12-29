n, s = [int(x) for x in input().split()]
menor = 1001

while n:
    n -= 1
    s += int(input())
    if s < menor:
        menor = s


print(menor)
