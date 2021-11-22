simbolos=['@','&','!','*','#']
letras=['a','e','i','o','u']
while True:
    try:
        s=input()
        for i in range(5):
            s=s.replace(simbolos[i],letras[i])
        print(s)
    except EOFError:break
