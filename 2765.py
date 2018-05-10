while True:
    try:
        c = input()
        c = c.split(',')
        for i in c:
            print(i)
    except EOFError:
        break