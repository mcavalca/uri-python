texto = input().split()
for i in range(len(texto)):
    if len(texto[i]) > 3:
        if texto[i][0:1] == texto[i][2:3]:
            texto[i] = texto[i][2:]

texto = ' '.join(texto)
print(texto)
