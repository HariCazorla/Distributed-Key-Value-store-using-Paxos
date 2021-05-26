import http.server
import logging
from datetime import datetime
from Constants import SERVER_PORT
from Exceptions import InvalidPathException
from Router import RouteHandler


class PaxosHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Class to handle the HTTP GET, PUT Requests
    """

    def _initialise(self):
        """
        Creates an object of RouteHandler
        """
        self.routeHandler = RouteHandler(self.path, self.command)

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
            self.routeHandler.validate()
            self._set_response(200)
            logging.info("[%s] %s", str(datetime.now()),
                         str(self.routeHandler))
        except InvalidPathException:
            self._set_response(404)
            logging.error("[%s] %s", str(datetime.now()),
                          str(self.routeHandler))

        self.wfile.write("GET request for {}".format(
            self.path).encode('utf-8'))

    def do_POST(self):
        """
        Executes the HTTP POST requests
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.debug("[%s]\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                      str(datetime.now()), str(self.path), str(self.headers), post_data.decode('utf-8'))
        try:
            self._initialise()
            self.routeHandler.validate()
            self._set_response(200)
            logging.info("[%s] %s", str(datetime.now()),
                         str(self.routeHandler))
        except InvalidPathException:
            self._set_response(404)
            ("[%s] %s", str(datetime.now()), str(self.routeHandler))

        self.wfile.write("POST request for {}".format(
            self.path).encode('utf-8'))


def run(server_class=http.server.HTTPServer, handler_class=PaxosHttpRequestHandler):
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
