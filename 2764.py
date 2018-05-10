while True:
    try:
        c = input()
        c = c.split('/')
        x = c[0]
        print('%s/%s/%s' %(c[1], c[0], c[2]))
        print('%s/%s/%s' %(c[2], c[1], c[0]))
        print('%s-%s-%s' %(c[0], c[1], c[2]))
        
    except EOFError:
        break