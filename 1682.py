c = 'NON'
for i in range(3, 5001):
    p = c + 'N'
    for j in range(3, i):
        if c[:j] in p:
            p = c + 'O'
            break
    for j in range(3, i):
        if c[:j] in p:
            p = c + 'P'
            break
    c = p
    
        
        
while True:
    n = int(input())
    if n == 0:
        break
    print(c[:n])
    