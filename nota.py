b = int(input())
t = int(input())

area = 160*70

areaesquerda = ((b + t)*70)/2

if areaesquerda == (area/2):
    print(0)
elif areaesquerda > (area/2):
    print(1)
else:
    print(2)