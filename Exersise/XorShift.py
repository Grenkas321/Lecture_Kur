state, n, a, b = eval(input())

for _ in range (n):
    state ^= state << 7
    state &= 0xFFFFFFFFFFFFFFFF
    state ^= state >> 9
    state &= 0xFFFFFFFFFFFFFFFF

print((state % (b - a + 1)) + a)
