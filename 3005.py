def emp(a,b):
    if ((((a[0] < b[0]) and (a[1] < b[1])) or ((a[0] < b[1]) and (a[1] < b[0]))) or (((a[0] < b[1]) and (a[1] < b[2])) or ((a[0] < b[2]) and (a[1] < b[1]))) or (((a[0] < b[0]) and (a[1] < b[2])) or ((a[0] < b[2]) and (a[1] < b[0])))):return True
    elif ((((a[1] < b[0]) and (a[2] < b[1])) or ((a[1] < b[1]) and (a[2] < b[0]))) or (((a[1] < b[1]) and (a[2] < b[2])) or ((a[1] < b[2]) and (a[2] < b[1]))) or (((a[1] < b[0]) and (a[2] < b[2])) or ((a[1] < b[2]) and (a[2] < b[0])))):return True
    elif ((((a[0] < b[0]) and (a[2] < b[1])) or ((a[0] < b[1]) and (a[2] < b[0]))) or (((a[0] < b[1]) and (a[2] < b[2])) or ((a[0] < b[2]) and (a[2] < b[1]))) or (((a[0] < b[0]) and (a[2] < b[2])) or ((a[0] < b[2]) and (a[2] < b[0])))):return True
    return False
for _ in range(int(input())):
    x=list(map(int,input().split()))
    p=[x[0],x[1],x[2]]
    s=[x[3],x[4],x[5]]
    if emp(p,s) and emp(s,p):print(3)
    elif emp(p,s):print(1)
    elif emp(s,p):print(2)
    else:print(0)
