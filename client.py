import socket

s = socket.socket()
host = socket.gethostname()
host = '0.0.0.0'
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close()
