import socket
import random

serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1", 1234))
serverSocket.listen()

clientSocket, addr = serverSocket.accept()
clientSocket.send (b"Pogodite zamisljeni broj od 1 do 10: ")
broj = clientSocket.recv(32).decode("utf-8")
broj = int(broj)
print (broj)

randomBroj = random.randint(1,10)


if broj == randomBroj:

    clientSocket.send (b"Pogodili ste zamisljeni broj!")

else:

    negativanOdgovor = f"Niste pogodili zamisljeni broj! Zamisljeni broj je {randomBroj}".encode("utf-8")
    clientSocket.send(negativanOdgovor)


 
