import socket as s


# TCP 
# AF_INET -> IPV4
# socketURL.send(b"GET / HTTP/1.1\r\nHost: {URL}\r\n\r\n")

# puerto que utiliza el serverpara comunicarse
serverDir = 'localhost'
serverPort = 50366 

tcpSocketServ = s.socket(s.AF_INET, s.SOCK_STREAM)
tcpSocketServ.bind(('', serverPort))
# ya su handshake
tcpSocketServ.listen(1)
print("TCP Server listening to port", serverPort)

while 1:
    tcpSocketClient, clientDir = tcpSocketServ.accept()

    message = tcpSocketClient.recv(2048).decode()
    if message == "terminate":
        break
    response = message.upper()

    print("se reviejde", message)
    tcpSocketClient.send(message.encode())
    tcpSocketClient.close()

"""
# UDP SERVER
# 49152 .. 65535
serverPort = 50365
# SOCK_DGRAM -> indica UDP
UdpSocketServ  = s.socket(s.AF_INET, s.SOCK_DGRAM)

UdpSocketServ.bind(('', serverPort))

print('Servidor escuchando en puerto:', serverPort)

while 1:
    message, clientDir = UdpSocketServ.recvfrom(2048)
    decoded = message.decode()

    print('Se recibio: ', decoded)
    respuesta = message.decode()

    answer = 'Answer: '+ decoded.upper()
    socketServ.sendto(answer.encode(), clientDir)

"""