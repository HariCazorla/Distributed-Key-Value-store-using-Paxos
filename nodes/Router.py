from Exceptions import InvalidPathException
from Constants import MAX_KEY_LENGTH


class RouteHandler:
    """
    Class to perform routing functionalities
    """

    def __init__(self, urlPath, reqType) -> None:
        self.urlPath = urlPath
        self.reqType = reqType
        pass

    def __repr__(self) -> str:
        return f'Handling {self.reqType} request for "{self.urlPath}"'

    def __str__(self) -> str:
        return f'Handling {self.reqType} request for "{self.urlPath}"'

    def validate(self):
        if self.reqType == 'GET' or self.reqType == 'POST':
            if str(self.urlPath).count('/') > 1:
                raise InvalidPathException
            if str(self.urlPath).__len__() > MAX_KEY_LENGTH:
                raise InvalidPathException
