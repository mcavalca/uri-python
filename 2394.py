n, m = [int(i) for i in input().split()]
j = []
while n:
    n -= 1
    j.append(sum([int(i) for i in input().split()]))
print(j.index(min(j))+1)
