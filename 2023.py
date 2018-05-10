l = []
while True:
    try:
        l.append(input())   
        
    except EOFError:
        break

l = sorted(l, key=lambda s: s.lower())
print(l[len(l)-1])