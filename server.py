import socket
import struct
import json
import hashlib as hl

class Connection():
	def __init__(self, port = 8080):
		self.socket = socket.socket()
		host = socket.gethostname()
		print(host, ':', port)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind(('0.0.0.0', port)) #Open to all by default
	
	def start(self):
		self.socket.listen(5)
		c, addr = self.socket.accept()
		print('Connection from', addr)
		self.authenticate(c)

	def auth(self, usernameHash, passwordHash):
		with open('config.json') as f:
			data = json.load(f)
			correctUsername = hl.md5(data['username'].encode()).digest() == usernameHash
			correctPassword = hl.md5(data['password'].encode()).digest() == passwordHash
		if correctPassword and correctUsername:
			return True
		else:
			return False

	def authenticate(self, c):
		numSupportedMethods = struct.pack('b', 3)
		supportedMethods = struct.pack('bbb', 1,2,3)
		c.send(numSupportedMethods)
		c.send(supportedMethods)
		method = struct.unpack('b', c.recv(1))[0]
		if method == 1:
			data = c.recv(32)
			usernameHash = data[:16]
			passwordHash = data[16:]
			if self.auth(usernameHash, passwordHash):
				c.send(b'Authentication Successful')
				c.close()


d = Connection()
d.start()