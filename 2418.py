nota = [float(x) for x in input().split()]
nota.sort()
final = sum(nota) - nota[0] - nota[-1]
print("%.1f" % final)
