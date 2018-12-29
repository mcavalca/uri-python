n = int(input())
consumo = 7
if n >= 101:
    consumo += (n - 100) * 5 + 160
elif n >= 31:
    consumo += (n - 30) * 2 + 20
elif n >= 11:
    consumo += n - 10

print(consumo)
