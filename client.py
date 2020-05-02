import socket as s

# variables de servidor
serverDir = "localhost"
tcpServerPort = 51366
udpServerPort = 0


while True:

    # TCP client
    # handshake
    tcpSocketClient = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpSocketClient.connect((serverDir, tcpServerPort))

    # recepcion url a buscar en el servidor
    toSend = input("Ingrese URLE: ")
    if toSend == "terminate":
        tcpSocketClient.send(toSend.encode())
        print("Se corto la wea")
        break

    # envio mensaje a servidor
    tcpSocketClient.send(toSend.encode())

    # recepcion de puerto UDP from server
    newPort = tcpSocketClient.recv(2048).decode()
    print("El puerto a usar para UDP es:", newPort)

    # cast a int para usar puerto udp
    udpServerPort = int(newPort)

   
   
   
    # UDP client
    # Inicio conexion UDP
    udpSocketClient  = s.socket(s.AF_INET, s.SOCK_DGRAM)
    print("")   
    toSend = input('Enviar: ')
    while toSend.lower() != "ok":
        toSend = input("Enviar ok plz: ")
        
    udpSocketClient.sendto(toSend.encode(), (serverDir, udpServerPort))

    # recepcion header
    messageToDecode, _ = udpSocketClient.recvfrom(2048)
    message = messageToDecode.decode()
    if message != "" and message != "Escriba OK  >_<":
        print("Header Recibido.")
        
    elif message == "Escriba OK  >_<":
        print("\n"+message)
    
    # cierre conexion UDP
    udpSocketClient.close()
    # cierre conexion TCP
    tcpSocketClient.close()


