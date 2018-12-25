t = int(input())
while t > 0:
    t -= 1
    n, k = input().split()
    n = int(n)
    k = int(k)
    total = int(int(n % k) + int(n / k))
    print(total)
