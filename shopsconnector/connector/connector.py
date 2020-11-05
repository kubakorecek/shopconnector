from requests import Session, Request
from shopsconnector.connector.utils import deserilize_json,serilize_json
from functools import wraps

# TODO: Finish commenting
# TODO: Think about renaming the scripts.
# TODO: Parametric test.

class _ReqMethod:
    DEFAULT = 'GET'
    POST = 'POST'
    GET = 'GET'
    

def _prepare_request(method=_ReqMethod.DEFAULT):
    """
    Decorator, with parametrs to be set from constants ReqMethod.
    :return:
    """
    def outer(func):
        def wrapper(self):
            self._req = Request(method=method,
                                url=self._url,
                                data=self._data,
                                headers=self._header
                                ).prepare()
            func(self)

        return wrapper()

    return outer


class ConnectionManager(object):
    """
        This class is managing resources.
    """

    def __init__(self,url, header= None, data = None, auth = None):
        self._header = header
        self._url = url
        self._data = data
        self._auth = auth
        self.__Test = None

    def __enter__(self):
        self.req = Session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.req.close()
        print('Clossing all connections')

    @_prepare_request(_ReqMethod.POST)
    def post(self):
        resp = self.req.send(self._Test)
        resp.raise_for_status()
        return resp.status_code, resp.text

    @_prepare_request(_ReqMethod.POST)
    def get(self):
        resp = self.req.send(self._prepare_request(_ReqMethod.GET))
        resp.raise_for_status()
        return resp.status_code, resp.text


