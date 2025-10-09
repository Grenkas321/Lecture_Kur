def ADD(f, g):
    def h(x):
        f_val = f(x) if callable(f) else f
        g_val = g(x) if callable(g) else g
        return f_val + g_val
    return h

def SUB(f, g):
    def h(x):
        f_val = f(x) if callable(f) else f
        g_val = g(x) if callable(g) else g
        return f_val - g_val
    return h

def MUL(f, g):
    def h(x):
        f_val = f(x) if callable(f) else f
        g_val = g(x) if callable(g) else g
        return f_val * g_val
    return h

def DIV(f, g):
    def h(x):
        f_val = f(x) if callable(f) else f
        g_val = g(x) if callable(g) else g
        return f_val / g_val
    return h