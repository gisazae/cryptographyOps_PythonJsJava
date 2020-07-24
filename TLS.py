# openssl req -new -x509 -keyout key.pem -out server1.pem -days 365 -nodes
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='server.pem', server_side=True)

httpd.serve_forever()
