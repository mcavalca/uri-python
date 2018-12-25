n = int(input())
h = [int(x) for x in input().split()]
if n == 2 and h[0] == h[1]:
    pico = 0
else:
    pico = 1
    for i in range(1, n-1):
        if not ((h[i] < h[i-1] and h[i] < h[i+1]) or (h[i] > h[i-1] and h[i] > h[i+1])):
            pico = 0
            break
print(pico)
