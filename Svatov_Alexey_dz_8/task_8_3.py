from functools import wraps


def type_logger(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        nonlocal cache
        for arg in args:
            cache.setdefault(arg, type(arg))
        for key, value in cache.items():
            print(f'{func.__name__}({key}: {value})')
        return cache

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 6, 'abc')
