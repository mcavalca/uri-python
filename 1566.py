# Counting sort has O(n + k), which is the fastest
# (that I could find)
def count_sort(vetor, maior):
    n = len(vetor)
    m = maior + 1
    count = [0] * m
    for i in vetor:
        count[i] += 1
    j = 0
    for i in range(m):
        for k in range(count[i]):
            vetor[j] = i
            j += 1
    return vetor

nc = int(input())
while nc:
    nc -= 1
    n = int(input())
    vetor = input().split()
    for i in range(len(vetor)):
        vetor[i] = int(vetor[i])

    vetor = count_sort(vetor, max(vetor))

    print(' '.join(str(x) for x in vetor))
