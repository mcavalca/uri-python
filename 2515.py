n = int(input())
pacote = [int(x) for x in input().split()]
l = 0
r = sum(pacote)
b = 0
print(r, l)
while l < r and b < (n-1):
    l += pacote[b]
    r -= pacote[b]
    b += 1

if l < r:
    l, r = r, l

print(r, l)
