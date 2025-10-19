import math

data = []
while True:
    line = input().strip()
    if not line or ' ' not in line:
        break
    parts = line.split()
    x, y, z = map(float, parts[:3])
    name = parts[3]
    data.append((x, y, z, name))

max_dist = -1
gal_1 = None
gal_2 = None

for i in range(len(data)):
    for j in range (i+1, len(data)):
        x1,y1,z1,name1 = data[i]
        x2,y2,z2,name2 = data[j]


        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        if dist > max_dist:
            max_dist = dist
            gal_1, gal_2 = name1, name2

print(*(sorted([gal_1, gal_2])))