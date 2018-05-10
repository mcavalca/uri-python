while True:
    try:
        cpf = input()
        cpf = cpf.replace('-', '.')
        cpf = cpf.split('.')
        for i in cpf:
            print(i)
        
    except EOFError:
        break