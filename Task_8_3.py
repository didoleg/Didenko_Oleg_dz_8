from functools import wraps


def cube_logger(func):
    @wraps(func)
    def wrapper(*args):
        for number in args:
            log_number = f'{func.__name__}({number}: {type(number)}, {number ** 3})'
            print(log_number)
        return func(*args)
    return wrapper


@cube_logger
def calc_cube(*args):
    """This functional get cube number"""
    return list(map(lambda x: x ** 3, args))


number_cube = calc_cube(4, 2)

print(number_cube)
print(calc_cube.__name__)
