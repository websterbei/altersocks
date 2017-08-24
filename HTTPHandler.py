from http.server import BaseHTTPRequestHandler as base
import requests

class HTTPHandler(base):
	def do_GET(self):
		print('GET')
		return requests.get(self.path).text

	def do_CONNECT(self):
		print('CONNECT')
		return requests.get('https://'+self.path.split(':')[0]).text