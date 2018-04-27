m = int(input())
alph = []
for i in range(65, 91):
    alph.append(chr(i))

for j in range(m):
    total = 0
    n = int(input())
    a = input()
    for i in range(n):
        if(a[i] != alph[i]):
            total += 1
    if(total < 3):
        print("There are the chance.")
    else:
        print("There aren't the chance.")
