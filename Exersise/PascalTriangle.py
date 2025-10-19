def pastri(n, filler):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    str_triangle = [[str(x) for x in row] for row in triangle]
    last_line = filler.join(str_triangle[-1])
    max_width = len(last_line)
    
    result_lines = []
    for row in str_triangle:
        line = filler.join(row)
        padding = max_width - len(line)
        left_padding = padding // 2
        right_padding = padding - left_padding
        
        result_lines.append(filler * left_padding + line + filler * right_padding)
    
    return "\n".join(result_lines)
