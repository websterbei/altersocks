import socket
import hashlib as hl
import struct

class Connection():
    def __init__(self, server_address, port):
        self.rsocket = socket.socket()
        self.rhost = server_address
        self.rport = port
        try:
            self.rsocket.connect((self.rhost, self.rport))
        except Exception as e:
            print(str(e))

    def authenticate(self, **kwargs):
        nMethods = struct.unpack('b', self.rsocket.recv(1))[0]
        methods = struct.unpack('{}b'.format(nMethods),
                                self.rsocket.recv(nMethods))
        print('Server Supported Authentication Methods: ', methods)
        if not kwargs['method'] in methods:
            raise Exception('Unsupported authentication method')
        if kwargs['method'] == 1:  #username, password authentication
            try:
                username = kwargs['username']
                password = kwargs['password']
            except:
                print('Missing username and/or password')
            self.rsocket.send(struct.pack('b', kwargs['method']))
            usernameHash = hl.md5(username.encode()).digest()
            passwordHash = hl.md5(password.encode()).digest()
            self.rsocket.send(usernameHash + passwordHash)
            authResponse = self.rsocket.recv(1024)
            if authResponse == b'Authentication Successful':
                self.listenLocal(9999)
            else:
                print('Authentication Failed')