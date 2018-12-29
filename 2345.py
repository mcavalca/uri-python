jog = [int(x) for x in input().split()]
jog.sort()
dif = abs((jog[0] + jog[3]) - (jog[1] + jog[2]))
print(dif)
