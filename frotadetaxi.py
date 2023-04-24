pa,pg,ka,kg = map(float,input().split())

ra = ka/pa
rg = kg/pg

if ra > rg:
    print('A')
elif ra <= rg:
    print('G')