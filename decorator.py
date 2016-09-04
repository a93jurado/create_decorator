import functools

def decorator(declared_decorator):
    """Create a decorator out of a function, which will be used as a wrapper."""
    @functools.wraps(declared_decorator)
    def final_decorator(func=None, **kwargs):
        def decorated(func):
            @functools.wraps(func)
            def wrapper(*a, **kw):
                return declared_decorator(func, a, kw, ** kwargs)
            return wrapper
        if func is None:
            return decorated
        else:
            return decorated(func)
    return final_decorator