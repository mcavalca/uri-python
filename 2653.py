l = []

while True:
    try:
        l.append(input())
        
    except EOFError:
        break
        
l = set(l)
print(len(l))