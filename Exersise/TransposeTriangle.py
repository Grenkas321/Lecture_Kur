lines = []
while True:
    line = input().strip()
    if line == '':
        break
    lines.append(line)

N = len(lines)
triangle = []
for line in lines:
    numbers = [int(x.strip()) for x in line.split(',')]
    triangle.append(numbers)

new_triangle = []
for i in range(N):
    new_row = []
    for k in range(i, -1, -1):
        row_index = N - 1 - k
        col_index = N - 1 - i
        new_row.append(triangle[row_index][col_index])
    new_triangle.append(new_row)

for i, row in enumerate(new_triangle):
    indent = ' ' * (N - i - 1)
    print(indent + ', '.join(map(str, row)))