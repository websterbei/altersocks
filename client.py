import socket
import hashlib as hl
import binascii as ba
import struct

class Connection():
	def __init__(self, server_address, port):
		self.socket = socket.socket()
		self.rhost = server_address
		self.rport = port
		try:
			self.socket.connect((self.rhost, self.rport))
		except Exception as e:
			print(str(e))

	def authenticate(self, **kwargs):
		nMethods = struct.unpack('b', self.socket.recv(1))[0]
		methods = struct.unpack('{}b'.format(nMethods), self.socket.recv(nMethods))
		print('Server Supported Authentication Methods: ', methods)
		if not kwargs['method'] in methods:
			raise Exception('Unsupported authentication method')
		if kwargs['method'] == 1: #username, password authentication
			try:
				username = kwargs['username']
				password = kwargs['password']
			except:
				print('Missing username and/or password')
			self.socket.send(struct.pack('b', kwargs['method']))
			usernameHash = hl.md5(username.encode()).digest()
			passwordHash = hl.md5(password.encode()).digest()
			self.socket.send(usernameHash+passwordHash)
			print(self.socket.recv(1024))

d = Connection('127.0.0.1', 8080)
d.authenticate(method = 1, username = 'testUser', password = 'defaultpasswd')
