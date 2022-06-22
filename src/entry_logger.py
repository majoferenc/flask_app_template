import logging

# At the beginning of every .py file in the project
def logger(fn):
    from functools import wraps
    import inspect
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logging.debug('Enter: %s' % fn.__name__)

        out = fn(*args, **kwargs)

        logging.debug('Exit: %s' % fn.__name__)
        # Return the return value
        return out
    return wrapper
