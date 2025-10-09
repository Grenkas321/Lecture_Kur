def pattsort(pattern, seq):
    pattern_indices = sorted(range(len(pattern)), key=lambda i: pattern[i])

    sorted_seq = sorted(seq)    
    result = [0] * len(seq)

    for i, pos in enumerate(pattern_indices):
        result[pos] = sorted_seq[i]
    
    return result
