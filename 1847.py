a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if(a > b):
    if c > b:
        print(':)')
    else:
        if(b-c < a-b):
            print(':)')
        else:
            print(':(')
            
    
elif(a < b):
    if c < b:
        print(':(')
    else:
        if(b-c > a-b):
            print(':(')
        else:
            print(':)')
    
else:
    if c > a:
        print(':)')
    else:
        print(':(')