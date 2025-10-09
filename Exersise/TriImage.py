rectangles = []
while True:
    line = input().strip()
    if line == "":
        break
    parts = line.split()
    x, y, w, h, char = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), parts[4]
    rectangles.append((x, y, w, h, char))

if not rectangles:
    exit()

min_x = min_y = float('inf')
max_x = max_y = float('-inf')

for x, y, w, h, char in rectangles:
    if w >= 0:
        x1, x2 = x, x + w
    else:
        x1, x2 = x + w, x
    
    if h >= 0:
        y1, y2 = y, y + h
    else:
        y1, y2 = y + h, y
    
    if x1 == x2 or y1 == y2:
        continue
        
    min_x = min(min_x, x1)
    max_x = max(max_x, x2)
    min_y = min(min_y, y1)
    max_y = max(max_y, y2)

if min_x == float('inf'):
    exit()

width = max_x - min_x
height = max_y - min_y
canvas = [['.' for _ in range(width)] for _ in range(height)]

for x, y, w, h, char in rectangles:
    if w >= 0:
        x1, x2 = x, x + w
    else:
        x1, x2 = x + w, x
    
    if h >= 0:
        y1, y2 = y, y + h
    else:
        y1, y2 = y + h, y
    
    if x1 == x2 or y1 == y2:
        continue
    
    for i in range(max(y1, min_y), min(y2, max_y)):
        for j in range(max(x1, min_x), min(x2, max_x)):
            canvas[i - min_y][j - min_x] = char

for row in canvas:
    print(''.join(row))