j = 0
while True:
    n = input()
    if int(n) < 0:
        break
    if('0x' in n):
        r = int(n[2:len(n)], 16)
    else:
        r = hex(int(n))
    print(r)