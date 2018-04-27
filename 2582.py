song = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY', 'SALT','ANSWER!','RAR?','WIFI ANTENNAS']
n = int(input())
while(n>0):
    n -= 1
    x, y = input().split()
    print(song[int(x)+int(y)])