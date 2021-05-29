from datetime import date, datetime
import logging
import requests
from uuid import uuid1
import os
import json
from Exceptions import *

PEERS = ['node1', 'node2', 'node3']


class Proposer:
    """
    Implementation of simple paxos algorithm
    """

    def __init__(self) -> None:
        pass

    def _sendLearnMessage(self, body=None):
        logging.info("[%s] sending Learn %s message to all peers...",
                     str(datetime.now()), str(body))
        paramerters = json.loads(body.decode('utf-8'))
        logging.info(" paramerters %s", str(paramerters))
        keys = paramerters.keys()
        logging.info(" keys %s", str(keys))
        values = paramerters.values()
        logging.info(" values %s", str(values))
        urlParamerters = {}
        for key in keys:
            urlParamerters["key"] = key
            break
        for val in values:
            urlParamerters["value"] = val
            break

        logging.info("[%s] sending Learn %s message to all peers...",
                     str(datetime.now()), str(urlParamerters))
        for peer in PEERS:
            url = "http://{}:8082/learn".format(peer)
            logging.info("[%s] URL: %s", str(datetime.now()), url)
            requests.get(url, params=urlParamerters)

    def _sendAcceptMessage(self, urlParamerters, body=None):
        logging.info("[%s] sending accept message to all peers...",
                     str(datetime.now()))
        acceptedPeerCount = 0
        majority = (len(PEERS) // 2) + 1
        for peer in PEERS:
            url = "http://{}:8082/accept".format(peer)
            res = requests.get(url, params=urlParamerters)

            if (res.status_code == 200):
                acceptedPeerCount += 1

            if (acceptedPeerCount >= majority):
                self._sendLearnMessage(body)
                break
        if (acceptedPeerCount < majority):
            raise AcceptRequestMajorityException

    def _sendPrepareMessage(self, body):
        logging.info("[%s] Sending prepare msg to all peers...\n",
                     str(datetime.now()))
        uuidString = uuid1()
        sid = os.getenv('SERVER_ID')
        proposalNumber = "{}.{}".format(uuidString, sid)
        urlParamerters = {}
        urlParamerters["proposalNumber"] = proposalNumber
        acceptedPeerCount = 0
        majority = (len(PEERS) // 2) + 1
        for peer in PEERS:
            # if sid != peer:
            url = "http://{}:8082/prepare".format(peer)
            logging.info("[%s] URL: %s", str(datetime.now()), url)
            res = requests.get(url, params=urlParamerters)
            logging.info("[%s] URL: %s", str(
                datetime.now()), str(res.status_code))
            if (res.status_code == 200):
                acceptedPeerCount += 1

            if (acceptedPeerCount >= majority):
                self._sendAcceptMessage(urlParamerters, body)
                break

        if (acceptedPeerCount < majority):
            raise PrepareRequestMajorityException

    def run(self, body):
        self._sendPrepareMessage(body)
