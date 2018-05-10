key = 'abcdefghijklmnopqrstuvxwyz'
cor = 'abcdefghijklmnopqrstuvxwyz'
n, m = input().split()
for i in range(int(n)):
    e, s = input().split()
    key = key.replace(e, '1')
    key = key.replace(s, '2')
    key = key.replace('1', e)
    key = key.replace('2', s)
for i in range(int(m)):
    c = input()
    for j in range(len(c)):
        c = c.replace(cor[cor.index(c[j])],key[key.index(c[j])])
    print(c)