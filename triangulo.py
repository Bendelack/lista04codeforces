a, b, c, d = map(int,input().split())

if a + b <= c:
    print('S')
elif a + b <= d:
    print('S')
elif a + c <= b:
    print('S')
elif a + c <= d:
    print('S')
elif a + d <= b:
    print('S')
elif a + d <= c:
    print('S')

elif b + a <= c:
    print('S')
elif b + a <= d:
    print('S')
elif b + c <= a:
    print('S')
elif b + c <= d:
    print('S')
elif b + d <= c:
    print('S')
elif b + d <= a:
    print('S')

elif c + b <= a:
    print('S')
elif c + b <= d:
    print('S')
elif c + a <= b:
    print('S')
elif c + a <= d:
    print('S')
elif c + d <= a:
    print('S')
elif c + d <= b:
    print('S')

elif d + b <= c:
    print('S')
elif d + b <= a:
    print('S')
elif d + c <= b:
    print('S')
elif d + c <= a:
    print('S')
elif d + a <= c:
    print('S')
elif d + a <= b:
    print('S')
else:
    print('N')