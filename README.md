## A basic test of a decorator to create decorators

##### Example of use:

```
@decorator
def suppress_errors(func, args, kwargs, log_func=None):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        if log_func is not None:
            log_func(str(e))

def print_logger(message):
    print(message)

@suppress_errors(log_func=print_logger)
def example():
    return something

example()
```