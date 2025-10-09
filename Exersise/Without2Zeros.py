def No_2Zero(N, K):
    if N == 1:
        return K - 1
    
    a = [0] * (N + 1)
    b = [0] * (N + 1)
    
    a[1] = K - 1
    b[1] = 0
    
    for i in range(2, N + 1):
        a[i] = (a[i-1] + b[i-1]) * (K - 1)
        b[i] = a[i-1]
    
    return a[N] + b[N]
