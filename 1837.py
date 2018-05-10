a, b = input().split()
a = int(a)
b = int(b)
n = a
if a < b:
    n = a
    a = b
    b = n
q = 1
for i in range(b, a, b):
    q += 1
r = b*q - a
print(q, r)