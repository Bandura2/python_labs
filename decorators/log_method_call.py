"""python package with decorators"""


def log_method_call(func):
    """
    Decorator that print name of function before it work
    :param func: function that decorated
    :return: function
    """

    def wrapper(*args, **kwargs):
        print(f"Now use method: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
