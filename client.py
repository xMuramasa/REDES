
import socket as s

serverDir = "localhost"
serverPort = 50366

socketCliente = s.socket(s.AF_INET, s.SOCK_STREAM)
#funcion que realiza handshake
socketCliente.connect((serverDir, serverPort))

toSend = input("Ingrese URLE")
socketCliente.send(toSend.encode())

msg = socketCliente.recv(2048).decode()
print(msg)
socketCliente.close()

















"""
serverDir = 'localhost'
serverPort = 50365

socketClient  = s.socket(s.AF_INET, s.SOCK_DGRAM)

toSend = input('Ingresar texto a convertir: ')
socketClient.sendto(toSend.encode(), (serverDir, serverPort))

message, _ = socketClient.recvfrom(2048)
print(message.decode())
socketClient.close()
"""