n = int(input())
l = []
while n:
    n -= 1
    l.append(int(input()))

l = set(l)
print(len(l))
