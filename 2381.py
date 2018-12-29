n, k = [int(x) for x in input().split()]
alunos = []

while n:
    n -= 1
    alunos.append(input())

alunos.sort()
print(alunos[k - 1])
