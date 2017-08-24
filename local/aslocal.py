from HTTPHandler import HTTPHandler
import socketserver

class ASLocal():
    def __init__(self, port):
        self.listenLocal(port)

    def listenLocal(self, port=9999):
        Handler = HTTPHandler
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", port), Handler)
        print("Local Proxy Started at Port ", port)
        httpd.serve_forever()

d = ASLocal(9999)
