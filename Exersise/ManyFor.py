def manyfor(order, *sequences):
    iterators = [iter(seq) for seq in sequences]
    
    for idx in order:
        if idx < 0 or idx >= len(iterators):
            break
        
        try:
            yield next(iterators[idx])
        except StopIteration:
            break
