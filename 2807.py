fib = [1, 1]
for x in range(2, 41):
    fib.append(fib[x-1]+fib[x-2])
fib.sort(reverse=True)
n = int(input())
palavra = ''
for x in fib[41-n:]:
    palavra += str(x) + ' '

palavra = palavra[:-1]
print(palavra)
