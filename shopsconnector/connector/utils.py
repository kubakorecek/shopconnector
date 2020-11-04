from functools import wraps
from json import loads,dumps


def deserilize_json(func):
    """
    Simple decorator to deserilize functions.
    :param func: fuction for decorator.
    :type func: fuction for decorator.
    :return: deserilized json of the function decorated with
    :rtype: deserilized json
    """
    @wraps(func)
    def _deserilize_json(*args, **kwargs):
        return loads(func(*args, **kwargs))
    return _deserilize_json


def serilize_json(func):
    """
    Simple decorator to serilize functions.
    :param func: fuction for decorator.
    :type func: fuction for decorator.
    :return: serilized json of the function decorated with
    :rtype: serilized json
    """
    @wraps(func)
    def _serilize_json(*args, **kwargs):
        return dumps(func(*args, **kwargs))
    return _serilize_json
