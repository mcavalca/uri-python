fat = [1, 2]
for x in range(3, 18):
    fat.append(x * fat[x-2])
    
while True:
    n = input()
    if n == '0':
        break
    print(fat[len(n)-1])