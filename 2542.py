n = int(input())
m, l = [int(x) for x in input().split()]

marcos = []
leo = []
for i in range(m):
    marcos.append([int(x) for x in input().split()])
for i in range(l):
    leo.append([int(x) for x in input().split()])

cm, cl = [int(x) for x in input().split()]
a = int(input())

marcos, leo = marcos[cm-1][a-1], leo[cl-1][a-1]
print(marcos, leo)

if marcos > leo:
    print('Marcos')
elif leo > marcos:
    print('Leonardo')
else:
    print('Empate')
