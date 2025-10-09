def factorizations(n, start=2, prefix=None):
    if prefix is None:
        prefix = []
    
    if start <= n:
        yield prefix + [n]
    
    for i in range(start, int(n**0.5) + 1):
        if n % i == 0:
            yield from factorizations(n // i, i, prefix + [i])

n = int(input())
for f in sorted(factorizations(n)):
    print(*f, sep = "*")