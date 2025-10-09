import random
import math

def randbits(p, n):
    if n < 1 or n > p:
        return 0
    count = math.comb(p, n)
    if count == 0:
        return 0

    k = random.randint(0, count - 1)
    
    result = 0
    remaining_bits = p
    remaining_ones = n
    
    for bit_pos in range(p - 1, -1, -1):       
        count_with_zero = math.comb(remaining_bits - 1, remaining_ones)
        
        if k >= count_with_zero:
            result |= (1 << bit_pos)
            k -= count_with_zero
            remaining_ones -= 1
        
        remaining_bits -= 1
    
    return result