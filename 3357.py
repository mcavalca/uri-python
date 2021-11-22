n,l,q=map(float,input().split())
s=input().split()
a=s[int((l//q)%len(s))]
b=l%q
print('Juca 0.4') if a=='Bob' and b==0.0 else print(f'{a} {b:.1f}')
