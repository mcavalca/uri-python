n = int(input())
let = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 's', 'S']

while n > 0:
    n -= 1
    c = input()
    var = 1
    for i in range(len(c)):
        if c[i] in let:
            var *= 3
        else:
            var *= 2
    
    print(var)