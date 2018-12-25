nota = input().split()
nota.sort()
final = 0
for x in nota:
    final += float(x)
final -= float(nota[0]) + float(nota[4])
print("%.1f" % final)
