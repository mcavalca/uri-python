n = int(input())
while(n > 0):
    n -= 1
    b, e = input().split()
    s = ''
    for i in range(int(b), int(e)+1):
        s += str(i)
    s += s[::-1]
    print(s)