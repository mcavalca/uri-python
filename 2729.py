n = int(input())
for i in range(n):
    a = input().split()
    a = sorted(set(a))
    print(' '.join(str(j) for j in a))
