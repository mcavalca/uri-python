n = input().split()
saida = "Otavio"
max = n[0]
if n[1] < max:
    saida = "Bruno"
    max = n[1]
if n[2] < max:
    saida = "Ian"
    max = n[2]
if n[0] == n[1] or n[1] == n[2] or n[2] == n[0]:
    saida = "Empate"

print(saida)