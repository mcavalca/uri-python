n = int(input())
k = int(input())
competidor = [int(input()) for x in range(n)]
competidor.sort(reverse=True)
total = k
while total < n and competidor[total] == competidor[k-1]:
    total += 1

print(total)
