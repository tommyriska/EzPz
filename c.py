import socket

HOST = '10.0.0.127'
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello World')
	
