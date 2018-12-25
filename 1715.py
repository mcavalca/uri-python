n, m = [int(x) for x in input().split()]
total = 0
while n:
    n -= 1
    gol = input().split()
    if gol.count('0') == 0:
        total += 1
        
print(total)
