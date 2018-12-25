iloveyou = [0] * 8

frase = input()

iloveyou[0] = frase.count('I')
iloveyou[1] = frase.count('l')
iloveyou[2] = int(frase.count('o')/2)
iloveyou[3] = frase.count('v')
iloveyou[4] = frase.count('e')
iloveyou[5] = frase.count('y')
iloveyou[6] = frase.count('u')
iloveyou[7] = frase.count('!')

print(min(iloveyou))
