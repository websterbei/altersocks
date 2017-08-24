from http.server import BaseHTTPRequestHandler as base
import socket as sk
import requests

class HTTPHandler(base):

    def do_GET(self):
        print('GET')
        self.wfile.write(requests.get(self.path).text.encode())

    def do_CONNECT(self):
        print('CONNECT')
        url = 'https://'+self.path.split(':')[0]
        print(url)
        self.wfile.write(requests.get(url).text.encode())

    def do_POST(self):
        print('POST')
        self.wfile.write(requests.post(self.path, headers=self.headers).text.encode())