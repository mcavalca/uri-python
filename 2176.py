message = input()
one = 0

for i in message:
    if i == '1':
        one += 1

print(message + str(one % 2))
