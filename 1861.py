murd = {}
ered = []

while True:
    try:
        kill, dead = input().split()
        if kill in murd:
            murd[kill] += 1
            ered.append(dead)
        else:
            murd[kill] = 1
            ered.append(dead)


    except EOFError:
        break


for i in ered:
    murd.pop(i, None)

print('HALL OF MURDERERS')

for i, v in sorted(murd.items()):
    print(i, v)
