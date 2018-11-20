from functools import wraps
from nakey.utils import codes


def response_wrapper():
    """
    Decorator to make a view only accept request with required http method.
    :param required http method.
    """
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            if response.data is None:
                response.data = dict()
            if not response.exception:
                response.data = {
                    "code": codes.OK,
                    "data": response.data
                }
            return response
        return inner
    return decorator
