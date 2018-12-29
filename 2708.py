turistas = 0
jipes = 0
while True:
    entrada = input().split()
    if entrada[0] == 'ABEND':
        break
    if entrada[0] == 'SALIDA':
        jipes += 1
        turistas += int(entrada[1])
    else:
        jipes -= 1
        turistas -= int(entrada[1])

print(turistas)
print(jipes)
