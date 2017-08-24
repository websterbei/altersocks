from http.server import BaseHTTPRequestHandler as base
import socket as sk
import requests

division = '''
===========================================================
===========================================================
===========================================================

'''


class HTTPHandler(base):

    def do_GET(self):
        print('GET')
        clientSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

        connectName = self.path.split(':')[1]
        port = 80
        slash_index = connectName.index("/", 2)
        print("before!!", connectName, "\nAfter!!!",  connectName[2:slash_index])


        ipAddr = sk.gethostbyname(connectName[2:slash_index])

        clientSocket.connect((ipAddr, port))
        clientSocket.send((str(self.requestline) + "\r\n" + str(self.headers)).encode())

        print (self.requestline , "\r\n" , self.headers)

        msg = clientSocket.recv(2048)

        clientSocket.close()
        self.wfile.write(msg)

    def do_CONNECT(self):
        print('CONNECT')

        clientSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

        connectName, port = self.path.split(':')
        port = int(port)
        print(connectName, port)

        ipAddr = sk.gethostbyname(connectName)

        clientSocket.connect((ipAddr, port))
        clientSocket.send((str(self.requestline) + "\r\n" + str(self.headers)).encode())

        print (self.requestline , "\r\n" , self.headers)
        msg = clientSocket.recv(2048)

        clientSocket.close()
        self.wfile.write(msg)
