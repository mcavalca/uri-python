def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

while True:
    n = int(input())
    if n == 0:
        break
    m = 0
    while is_power2(n) != True:
        if n > m:
            m = n
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n*3 + 1
    if n > m:
        m = n
    print(m)