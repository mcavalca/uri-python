import math

while True:
    try:
        l = float(input())
        x = l*(math.sin(0.6*math.pi)/math.sin(0.35*math.pi))
        # raio do pentagono circunscrito
        # h = l/(2*math.tan(0.2*math.pi))
        # print('Apotema: ', h)
        
        # apotema do pentagono
        # l = math.sqrt(h**2 + (l/2)**2)
        # print('Raio: ', l)
        
        # diagonal do quadrado
        # l += h
        
        # lado do quadrado
        # l = l/math.sqrt(2)
        
        print('%.10f'%x)
        
    except EOFError:
        break