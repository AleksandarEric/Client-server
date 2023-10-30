import socket

clientSocket = socket.socket()
clientSocket.connect(("127.0.0.1", 1234))

message = clientSocket.recv(256).decode("utf-8")
broj = input(message)
clientSocket.send(bytes(broj, "utf-8"))

rezultat = clientSocket.recv(256).decode("utf-8")
print (rezultat)

netacno = clientSocket.recv(256).decode("utf-8")
print (netacno)

tacno = clientSocket.recv(256).decode("utf-8")
print (tacno)
