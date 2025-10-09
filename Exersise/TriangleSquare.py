from decimal import Decimal, getcontext

getcontext().prec = 1000

data = input().strip()
parts = [x.strip() for x in data.split(',')]
x1, y1, x2, y2, x3, y3 = [Decimal(p) for p in parts]

area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / Decimal(2))

result_str = format(area, 'f')
if '.' in result_str:
    result_str = result_str.rstrip('0').rstrip('.')
print(result_str)
