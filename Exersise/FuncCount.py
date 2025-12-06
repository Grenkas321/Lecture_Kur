from functools import wraps

def counter(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)

    def get_count():
        return count

    wrapper.counter = get_count
    return wrapper
