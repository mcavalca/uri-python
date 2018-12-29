n = []
v = int(input())
n.append([v*x*2 for x in range(1,11)])
print(n)
for i in range(len(n)):
    print('N[%d] = %d' % (i, n[i]))
