a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

maior = a

if b > maior and b > c and b > d and b > e:
    maior = b
elif c > maior and c > b and c > d and c > e:
    maior = c
elif d > maior and d > b and d > c and d > e:
    maior = d
elif e > maior and e > b and e > c and e > d:
    maior = e

print(maior)