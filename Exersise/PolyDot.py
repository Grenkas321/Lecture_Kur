import math

def info(dots, dot):
    points = list(dots)
    n = len(points)
    
    # Вычисляем периметр с использованием math.hypot для лучшей точности
    perimeter = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        perimeter += math.hypot(x2 - x1, y2 - y1)
    
    # Проверяем выпуклость
    is_convex = True
    if n < 3:
        is_convex = False
    else:
        sign = 0
        for i in range(n):
            A = points[i]
            B = points[(i + 1) % n]
            C = points[(i + 2) % n]
            cross_product = (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])
            if cross_product != 0:
                if sign == 0:
                    sign = 1 if cross_product > 0 else -1
                else:
                    if (cross_product > 0 and sign < 0) or (cross_product < 0 and sign > 0):
                        is_convex = False
                        break
    
    # Проверяем принадлежность точки многоугольнику с помощью алгоритма трассировки луча
    inside = False
    if n >= 3:
        x, y = dot
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            # Проверяем, пересекает ли луч из точки вправо ребро многоугольника
            if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                inside = not inside
                
    return perimeter, is_convex, inside
