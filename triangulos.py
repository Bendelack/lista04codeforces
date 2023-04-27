a,b,c  = map(int,input().split())

if a + b > c and a + c > b and b + c > a:
    if ((a**2) + (b**2)) == (c**2) or ((a**2) + c**2) == (b**2) or ((c**2) + b**2) == (a**2):
        print('r')
    elif ((a**2) + (b**2)) < (c**2) or ((a**2) + c**2) < (b**2) or ((c**2) + b**2) < (a**2):
        print('o')
    else:
        print('a')
else:
    print('n')