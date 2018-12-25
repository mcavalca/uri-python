predio = [int(input()) for andar in range(3)]
tempo_gasto = []
tempo_gasto.append(predio[0]*4 + predio[1]*2)
tempo_gasto.append(predio[0]*2 + predio[2]*2)
tempo_gasto.append(predio[1]*2 + predio[2]*4)

tempo_gasto.sort()
print(tempo_gasto[0])
