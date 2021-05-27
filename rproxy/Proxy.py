import http.server
import requests
import itertools
import logging
from datetime import datetime

PAXOS_CLUSTER = ['node1', 'node2', 'node3']
LOAD_BALANCER = itertools.cycle(PAXOS_CLUSTER)
PAXOS_CLUSTER_PORT = ':8082'


class ProxyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Load balancer and Http reverse proxy implementation class.
    """

    def _getServer(self):
        """
        Roundrobin load balancer
        """
        server = next(LOAD_BALANCER)
        return server + PAXOS_CLUSTER_PORT

    def do_GET(self):
        """
        Forwards HTTP GET requests to paxos cluster.
        """
        logging.debug("[%s] \nPath: %s\nHeaders:\n%s\nCommand:\n%s\n",
                      str(datetime.now()), str(self.path), str(self.headers), str(self.command))

        hostname = self._getServer()
        url = 'http://{}{}'.format(hostname, self.path)
        logging.info("[%s] forwading url: %s", str(datetime.now()), url)
        resp = requests.get(url, headers=self.headers, verify=False)
        self.send_response(resp.status_code)
        self.wfile.write(resp.content)

    def do_POST(self):
        """
        Forwards HTTP POST requests to paxos cluster.
        """
        content_length = int(self.headers['Content-Length'])
        req_body = self.rfile.read(content_length)
        logging.debug("[%s]\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                      str(datetime.now()), str(self.path), str(self.headers), req_body.decode('utf-8'))
        hostname = self._getServer()
        url = 'http://{}{}'.format(hostname, self.path)
        logging.info("[%s] forwading url: %s", str(datetime.now()), url)
        resp = requests.get(url, headers=self.headers,
                            verify=False, data=req_body)
        self.send_response(resp.status_code)
        self.wfile.write(resp.content)


def run(server_class=http.server.HTTPServer, handler_class=ProxyHttpRequestHandler):
    """
    Starts a basic http server which takes requests and forwards
    it to the paxos cluster
    """
    logging.basicConfig(level=logging.INFO)
    server_address = ('', 8081)
    httpd = server_class(server_address, handler_class)
    logging.info('[%s] Starting Reverse proxy...\n', str(datetime.now()))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('[%s] Stopping Reverse proxy...\n', str(datetime.now()))


if __name__ == '__main__':
    run()
