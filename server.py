import socket as s

# TCP Server
# AF_INET -> IPV4
# socketURL.send(b"GET / HTTP/1.1\r\nHost: {URL}\r\n\r\n")
# puerto que utiliza el serverpara comunicarse
# 49152 .. 65535
serverDir = 'localhost'
serverPort = 51366
newServerPort = serverPort + 10

#sockets para conexion TCP
tcpSocketServ = s.socket(s.AF_INET, s.SOCK_STREAM)
tcpSocketServ.bind(('', serverPort))

# ya su handshake
tcpSocketServ.listen(2)
print("Servidor TCP escuchando en el puerto: ", serverPort)

cache = []

while 1:
    # Aceptar el mensaje del clienteTCP a servidorTCP
    tcpSocketClient, clientDir = tcpSocketServ.accept()
    message = tcpSocketClient.recv(2048).decode()

    # Terminar comunicacion
    if message == "terminate":
        print("Cago el server")
        break

    # Hacer el GET
    socketUrl = s.socket(s.AF_INET, s.SOCK_STREAM)
    socketUrl.connect((message, 80))   
    socketUrl.sendall(b'GET / HTTP/1.1\r\n\r\n')
    
    # recibir respuesta GET
    headReceived = socketUrl.recv(2048)
    header = headReceived.decode("cp437")
    
    # split header para cliente
    header = header.split("<")[0]
    cache.append(header)

    # respuesta servidor -> cliente
    toSend = str(newServerPort)
    tcpSocketClient.send(toSend.encode())
    print("Envio puerto UDP a cliente")
    
    # cierre de socket usados en TCP
    socketUrl.close()
    tcpSocketClient.close()
    
    # Inicio conexion UDP 

    # Sockets para conexion UDP
    udpSocketServ = s.socket(s.AF_INET, s.SOCK_DGRAM) # SOCK_DGRAM -> indica UDP
    udpSocketServ.bind(('', newServerPort))

    print('\nServidor UDP escuchando en el puerto:', newServerPort)
    print("Esperando respuesta cliente")

    message, clientDir = udpSocketServ.recvfrom(2048)
    decoded = message.decode()
    if decoded == "terminate":
        print("Cago el server")
        break

    print('Respuesta cliente: ', decoded)
    respuesta = message.decode()

    answer = 'Respuestaaaaaa: '+ header
    udpSocketServ.sendto(answer.encode(), clientDir)
        
    # cierre server UDP
    print("Cierre servidor UDP")
    udpSocketServ.close()
            

# cierre conexion TCP
tcpSocketClient.close()
tcpSocketServ.close()

