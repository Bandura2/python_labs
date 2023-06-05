"""python package with decorators"""
import subprocess


def run_pylint(func):
    """
    Decorator that run command pylint
    :param func: function that decorated
    :return: function
    """

    def wrapper(*args, **kwargs):
        subprocess.run(f"pylint {func.__code__.co_filename}", check=True)
        return func(*args, **kwargs)

    return wrapper
