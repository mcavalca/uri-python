def rem7(word):
    n = ''
    for i in range(len(word)):
        if word[i] == '7':
            n += '0'
        else:
            n += word[i]
    return int(n)

a, op, b = input().split()

a = rem7(a)
b = rem7(b)

if op == '+':
    a += b
else:
    a *= b

a = str(a)
a = rem7(a)
    
print(a)