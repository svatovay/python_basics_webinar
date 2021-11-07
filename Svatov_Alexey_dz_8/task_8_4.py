from functools import wraps


def val_checker(callback=lambda x: isinstance(x, int)):
    def _val_checker(func):
        @wraps(func)
        def wrapper(msg):
            if not callback(msg):
                raise ValueError(f'wrong val {msg}')
            else:
                result = func(msg)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
