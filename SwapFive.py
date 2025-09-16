k = int(input())

if k == 0 or k == 1:
    print(k)
    exit(0)

n = 1
while True:
    right = k * (10**n - k)
    if right % (10 * k - 1) == 0:
        x = right // (10 * k - 1)
        if 10**(n-1) <= x < 10**n:
            result = x * 10 + k
            print(result)
            break
    
    n += 1
