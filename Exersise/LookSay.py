def LookSay():
    from itertools import groupby
    
    sequence = [1]
    yield 1
    
    while True:
        next_sequence = []
        for digit, group in groupby(sequence):
            count = sum(1 for _ in group)
            next_sequence.extend([count, digit])
        
        for digit in next_sequence:
            yield digit
        
        sequence = next_sequence
