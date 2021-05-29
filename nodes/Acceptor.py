from datetime import datetime
import logging
from uuid import UUID
from urllib.parse import urlparse, parse_qs
from Exceptions import *


class Acceptor:
    def __init__(self) -> None:
        self._highestProposalNumber = ''
        pass

    def prepareHandler(self, urlpath):
        query_components = parse_qs(urlparse(urlpath).query)
        proposalPath = query_components["proposalNumber"][0]
        proposalUUID = proposalPath.split('.')[0]

        if ((proposalUUID == None) or (proposalUUID <= '')):
            raise InvalidProposalNumberException

        try:
            uuidVersion = UUID(proposalUUID).version
            if uuidVersion != 1:
                raise ValueError
        except ValueError:
            raise InvalidProposalNumberException

        if (proposalUUID < self._highestProposalNumber):
            raise InvalidProposalNumberException

        if (proposalUUID > self._highestProposalNumber):
            self._highestProposalNumber = proposalUUID

        logging.info("[%s] proposal number %s",
                     str(datetime.now()), proposalUUID)

    def acceptHandler(self, urlpath):
        logging.info("[%s] Accept msg handler pno - %s",
                     str(datetime.now()), self._highestProposalNumber)
        query_components = parse_qs(urlparse(urlpath).query)
        proposalPath = query_components["proposalNumber"][0]
        proposalUUID = proposalPath.split('.')[0]

        if ((proposalUUID == None) or (proposalUUID <= '')):
            raise InvalidProposalNumberException

        try:
            uuidVersion = UUID(proposalUUID).version
            if uuidVersion != 1:
                raise ValueError
        except ValueError:
            raise InvalidProposalNumberException

        if (proposalUUID < self._highestProposalNumber):
            raise InvalidProposalNumberException

        if (proposalUUID > self._highestProposalNumber):
            self._highestProposalNumber = proposalUUID

        logging.info("[%s] Accepted proposal number %s",
                     str(datetime.now()), proposalUUID)
