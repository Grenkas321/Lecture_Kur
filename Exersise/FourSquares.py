import math

N = int(input())
limit = int(math.isqrt(N)) + 1

result = set()

for x in range(limit + 1):
    for y in range(x, limit + 1):
        for z in range(y, limit + 1):
            rest = N - x*x - y*y - z*z
            if rest < 0:
                break
            t = int(math.isqrt(rest))
            if t >= z and t*t == rest:
                result.add(tuple(sorted([x, y, z, t], reverse=True)))

for sol in sorted(result):
    print(*sol)