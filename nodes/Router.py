import logging
from Constants import SERVER_PORT
from datetime import datetime
from Exceptions import *
from Constants import MAX_KEY_LENGTH
from Proposer import Proposer
from Acceptor import Acceptor
from Learner import Learner

PREPARE_REQUEST = "prepare"
ACCEPT_REQUEST = "accept"
LEARN_REQUEST = "learn"
KEY_REQUEST = "key"


class RouteHandler:
    """
    Class to perform routing functionalities
    """

    def __init__(self, urlPath, reqType, ks) -> None:
        self.urlPath = urlPath
        self.reqType = reqType
        self.proposer = Proposer()
        self.acceptor = Acceptor()
        self.learner = Learner()
        self.keystore = ks
        pass

    def __repr__(self) -> str:
        return f'Handling {self.reqType} request for "{self.urlPath}"'

    def __str__(self) -> str:
        return f'Handling {self.reqType} request for "{self.urlPath}"'

    def validate(self):
        if self.reqType == 'GET' or self.reqType == 'POST':
            if str(self.urlPath).count('/') > 1:
                raise InvalidPathException

    def setValue(self, body):
        logging.info(
            "[%s] Running Paxos consensus algorithm round", str(datetime.now()))
        self.proposer.run(body)

    def handle(self):
        response = "Welcome to the Distributed Key Value Store..."
        if PREPARE_REQUEST in self.urlPath:
            self.acceptor.prepareHandler(self.urlPath)
        elif ACCEPT_REQUEST in self.urlPath:
            self.acceptor.acceptHandler(self.urlPath)
        elif LEARN_REQUEST in self.urlPath:
            self.learner.learnHandler(self.urlPath, self.keystore)
        elif KEY_REQUEST in self.urlPath:
            response = self.learner.keyHandler(self.urlPath, self.keystore)
        else:
            logging.info("Other GET Request")
        return response
