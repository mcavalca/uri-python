fib = [0, 1, 1, 1, 2, 2]
for i in range(6, 20):
    if(((i-1) % 2) == 0):
        fib.append(fib[i-1]*fib[i-2])
    else:
        fib.append(fib[i-1]+fib[i-2])


while True:
    try:
        n = int(input())
        print(fib[n-1])
        
    except EOFError:
        break