b=int(input())
g=int(input())

if g%2!=0:g-=1
if g<=b*2:print("Amelia tem todas bolinhas!")
else:
    aux=(g-(2*b))/2
    print(f'Faltam {aux:.0f} bolinha(s)')
