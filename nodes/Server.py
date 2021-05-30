import http.server
from Store import KeyStore
from socketserver import ThreadingMixIn
import threading
import logging
from datetime import datetime
from Exceptions import *
from Constants import SERVER_PORT
from Exceptions import *
from Router import RouteHandler

ks = KeyStore()


class PaxosHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Class to handle the HTTP GET, PUT Requests
    """

    def _initialise(self):
        """
        Creates an object of RouteHandler
        """
        self.routeHandler = RouteHandler(self.path, self.command, ks)

    def _set_response(self, res):
        self.send_response(res)
        self.send_header('Content-Type', 'Text/html')
        self.end_headers()

    def do_GET(self):
        """
        Executes the HTTP GET requests
        """
        logging.debug("[%s] \nPath: %s\nHeaders:\n%s\nCommand:\n%s\n",
                      str(datetime.now()), str(self.path), str(self.headers), str(self.command))

        try:
            self._initialise()
            logging.info("[%s] %s", str(datetime.now()),
                         str(self.routeHandler))
            self.routeHandler.validate()
            res = self.routeHandler.handle()
            self._set_response(200)

        except InvalidPathException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          str(self.routeHandler))

        except InvalidProposalNumberException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          str(self.routeHandler))

        except KeyNotFoundException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          "Failed to fetch Key...")

        except UnexpectedException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()), str(
                "Failed due to an unexpected exception..."))

        self.wfile.write("response: {}".format(
            res).encode('utf-8'))

    def do_POST(self):
        """
        Executes the HTTP POST requests
        """
        content_length = int(self.headers['Content-Length'])
        req_body = self.rfile.read(content_length)
        logging.debug("[%s]\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                      str(datetime.now()), str(self.path), str(self.headers), req_body.decode('utf-8'))
        try:
            self._initialise()
            self.routeHandler.validate()
            logging.info("[%s] %s", str(datetime.now()),
                         str(self.routeHandler))
            self.routeHandler.setValue(req_body)
            self._set_response(200)

        except InvalidPathException:
            self._set_response(404)
            logging.error("[%s] Invalid path exception while %s", str(datetime.now()),
                          str(self.routeHandler))

        except PrepareRequestMajorityException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          "Failed to set the value becuase majority not reached...")

        except InvalidKeyValuePairException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          "Failed to update Key-store...")

        except UnexpectedException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()), str(
                "Failed to set Value due to an unexpected exception..."))

        self.wfile.write("Successful!".encode('utf-8'))


class ThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    """
    Handles each request in a seperate thread
    """


def run(server_class=ThreadedHTTPServer, handler_class=PaxosHttpRequestHandler):
    """
    Start a basic HTTP server instance that listens on port 8000
    """
    logging.basicConfig(level=logging.INFO)
    server_address = ('', SERVER_PORT)
    httpd = server_class(server_address, handler_class)
    logging.info('[%s] Starting httpd...\n', str(datetime.now()))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('[%s] Stopping httpd...\n', str(datetime.now()))


if __name__ == '__main__':
    run()
