n, m = input().split()
n = int(n)
m = int(m)
if(m <= 2 and m >= 0):
    print('nova')
elif(m <= 100 and m >= 97):
    print('cheia')
elif(m > n):
    print('crescente')
else:
    print('minguante')