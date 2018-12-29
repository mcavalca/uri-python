n, k = [int(i) for i in input().split()]
rooms = [int(i) for i in input().split()]
rooms.sort(reverse=True)
n = n//(k+1)
k = sum(rooms[n:])
print(rooms[:n],'AAAAAAAAAAAAAAAAAAA', rooms[n:])
print(len(rooms[:n]))
