while(True):
    a, b = input().split()
    carry = 0
    c = 0
    if((a == '0') and (b == '0')):
        break
    
    while(len(a) < len(b)):
        a = '0' + a
    while(len(b) < len(a)):
        b = '0' + b
    
    for i in reversed(range(0, len(a))):
        if ((int(a[i]) + int(b[i]) > 9) or ((int(a[i]) + int(b[i]) + c)) > 9):
            carry += 1
            c = 1
        else:
            c = 0
            
    if(carry == 0):
        print("No carry operation.")
    elif(carry == 1):
        print("1 carry operation.")
    else:
        print("%d carry operations." % carry)
    