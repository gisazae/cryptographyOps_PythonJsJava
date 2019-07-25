# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate {cert,key}
#    openssl req -new -x509 -keyout server.pem -out server1.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# 
#    https://localhost:4443

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server1.pem', server_side=True)
httpd.serve_forever()
