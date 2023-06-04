"""python package with decorators"""
import logging
import os


def logged(exception, mode):
    """
    Decorator that logged exception in console or file
    :param exception: type of exception that will be handled
    :param mode: indicates the mode in which the decorator will work;
    :return: function
    """
    if mode not in ["console", "file"]:
        raise ValueError("Invalid mode specified for logged decorator")

    def nested_logged(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                if mode == "console":
                    logging.basicConfig(format='%(levelname)s %(asctime)s\nmassage: %(message)s')
                    logging.error(exception(str(exception)))
                else:
                    relative_path = os.path.normpath(os.path.join(os.getcwd(), '..', 'error_logs'))
                    format_error = '\n%(levelname)s %(asctime)s\nmassage: %(message)s'
                    logging.basicConfig(filename=relative_path, format=format_error)
                    logging.error(exception(repr(exception)))

        return wrapper
    return nested_logged
