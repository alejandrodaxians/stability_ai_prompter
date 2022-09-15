from time import time


def check_runtime(call_func):
    def decorator_func(*args, **kwargs):
        # Pre decorator
        startTime = time()
        result = call_func(*args, **kwargs)
        # Post decorator
        executionTime = (time() - startTime)
        print(executionTime)
        return result
    return decorator_func
