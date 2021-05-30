from datetime import datetime
import logging
from Exceptions import *


class KeyStore:
    """
    In Memeory Dictionary which stores all the key value pairs
    """

    def __init__(self) -> None:
        self._keyStore = {}

    def ___repr__(self) -> str:
        return "Key store with {} entries...".format(len(self._keyStore.keys()))

    def __str__(self) -> str:
        return "Key store with {} entries...".format(len(self._keyStore.keys()))

    def getKey(self, key):
        try:
            return self._keyStore[key]
        except ValueError:
            raise KeyNotFoundException
        except KeyError:
            raise KeyNotFoundException

    def setKey(self, key, value):
        try:
            self._keyStore[key] = value
        except ValueError:
            raise InvalidKeyValuePairException
