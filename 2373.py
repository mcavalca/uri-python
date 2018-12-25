n = int(input())
quebrados = 0
while n > 0:
    n -= 1
    l, c = input().split()
    if int(c) < int(l):
        quebrados += int(c)

print(quebrados)
