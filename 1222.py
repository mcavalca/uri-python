n, l, c = input().split()
w = input()
page = 1
line = 0
ch = 0

for i in w:
    ch += 1
    if i == ' ' and ch == int(c):
        ch = 0
        line += 1        
    if ch == int(c):
        ch = 0
        line += 1
    if line == int(l):
        line = 0
        page += 1
    
print(page)