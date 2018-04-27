r = input()
comp = ''
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(len(r)):
    if r[i] in vowel:
        comp += r[i]
if(comp == comp[::-1]):
    print('S')
else:
    print('N')