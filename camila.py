# Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.
# Cibele > Camila > Celeste

a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a > c and a < b):
    print(a)
elif b > a and b < c or (b > c and b < a):
    print(b)
elif c > a and c < b or (c > b and c < a):
    print(c)
elif a == b and a == c:
    print(a)
elif (a == b and a != c) or (a == c and a != b):
    print(a)
elif (a == b and b != c) or (b == c and b != a):
    print(b)
elif (c == a and c != b) or (c == b and c != a):
    print(c)