from datetime import datetime
import logging
from typing import KeysView
from uuid import UUID
from urllib.parse import urlparse, parse_qs
from Store import KeyStore
from Exceptions import *


class Learner:
    def __init__(self) -> None:
        pass

    def learnHandler(self, urlPath, store):
        logging.info("[%s] Learn msg handler", str(datetime.now()))
        query_components = parse_qs(urlparse(urlPath).query)
        key = query_components["key"][0]
        value = query_components["value"][0]
        store.setKey(key, value)
        logging.info("[%s] Learnt %s and %s", str(datetime.now()), key, value)
        logging.info("[%s] ks instance %s", str(datetime.now()), str(store))

    def keyHandler(self, urlPath, store):
        logging.info("[%s] keys msg handler", str(datetime.now()))
        key = urlPath.split('=')[1]
        logging.info("[%s] key value is %s", str(datetime.now()), key)
        try:
            value = store.getKey(key)
        except KeyNotFoundException:
            value = "-"
        except ValueError:
            value = "-"
        logging.info("[%s] value is %s", str(datetime.now()), value)
        return str(value)
