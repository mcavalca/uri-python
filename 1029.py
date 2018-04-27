tot = 0

def fibo(f):
    global tot
    tot += 1
    if(f == 0):
        return 0
    elif(f == 1):
        return 1
    else:
        f = fibo(f-1) + fibo(f-2)
    return f
    
t = int(input())
while(t > 0):
    tot = -1
    n = int(input())
    f = fibo(n)
    print("fib(%d) = %d calls = %d" %(n, f[tot], f[i]))
    t -= 1