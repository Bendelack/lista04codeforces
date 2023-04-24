consumo   = int(input())
distancia = int(input())
atual     = int(input())

total = distancia/consumo

abastecer = total - atual

if abastecer > 0:
    print(f'{abastecer:.1f}')
else:
    print(0.0)

# 2km/l
# 10km
# 2

# precisa > 5km
#precisa = distancia/consumo