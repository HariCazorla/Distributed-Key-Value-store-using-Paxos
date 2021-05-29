from datetime import datetime
import logging
from uuid import UUID
from urllib.parse import urlparse, parse_qs


class Learner:
    def __init__(self) -> None:
        pass

    def learnHandler(self, urlPath):
        logging.info("[%s] Learn msg handler", str(datetime.now()))
        query_components = parse_qs(urlparse(urlPath).query)
        key = query_components["key"][0]
        value = query_components["value"][0]
        logging.info("[%s] Learnt %s and %s", str(datetime.now()), key, value)
