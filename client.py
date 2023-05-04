import socket

sock = socket.socket()
sock.setblocking(2)
sock.connect(('127.0.0.1', 1234))

print("Enter your message:")
Y = str(input())
sock.sendall(bytes(Y, "utf-8"))


sock.close()
