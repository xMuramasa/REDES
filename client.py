import socket as s

# variables de servidor
serverDir = "localhost"
tcpServerPort = 51366
udpServerPort = 0

def check(toSend):
    print("Termina la conexion")
    return 

conection = True
    
print("\n\t------>Conexion cliente TCP<------\n")

while True:
    #-------------------------------------------------> TCP client
    # handshake
    tcpSocketClient = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpSocketClient.connect((serverDir, tcpServerPort))

    # recepcion url a buscar en el servidor
    print("Enviar: \n\tURL http: si desa buscar una wea\n\tterminate: si desea terminar la conexion")
    url = input("\nIngrese URLE: ")

    # si se recive terminate, se termina la conexion
    if url == "terminate":
        print("\n\t------>Fin conexion con server<------\n")
        tcpSocketClient.send(url.encode())
        tcpSocketClient.close()
        break
    

    print("\n\t------>Inicio conexion UDP con server<------\n")
    # envio mensaje a servidor
    tcpSocketClient.send(url.encode())

    # recepcion de puerto UDP from server
    newPort = tcpSocketClient.recv(2048).decode()
    print("El puerto a usar para UDP es:", newPort)

    # cast a int para usar puerto udp
    udpServerPort = int(newPort)

    #---------------------------------------------------> UDP client
    # Inicio conexion UDP
    udpSocketClient  = s.socket(s.AF_INET, s.SOCK_DGRAM)
    print("Enviar: \n\tOk: si desea recibir header\n")
    toSend = input('Ingrese mensaje: ')
    
    while toSend.lower() != "ok":
        toSend = input('Ingrese mensaje: ')

    udpSocketClient.sendto(toSend.encode(), (serverDir, udpServerPort))
    # recepcion header
    messageToDecode, _ = udpSocketClient.recvfrom(2048)
    message = messageToDecode.decode()

    with open("cache/" + url + ".txt", "w") as urlData:
        if message != "":
            print("\n\t------>Header recibido<------\n")
            urlData.write(message)

    # cierre conexion UDP
    udpSocketClient.close()


    # cierre conexion TCP
tcpSocketClient.close()


