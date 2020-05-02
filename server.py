import socket as s
import json

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
tcpSocketServ.listen(1)

#read cache.txt
try:
    with open('cache.txt', 'r') as filehandle:
        cache = json.load(filehandle)
except(FileNotFoundError):
    cache = [ [int(0),"",""] , [int(0),"",""] , [int(0),"",""] , [int(0),"",""] , [int(0),"",""] ]
    with open('cache.txt', 'w') as filehandle:
        json.dump(cache, filehandle)


#cahe_i = [tiempo,url,header]
existe = 0
con = 0

while 1:
    print("Servidor TCP escuchando en el puerto: ", serverPort)
    # Aceptar el mensaje del clienteTCP a servidorTCP
    tcpSocketClient, clientDir = tcpSocketServ.accept()

    message = tcpSocketClient.recv(2048).decode()
    
    # header cualquier
    header = ""

    if message != "terminate":
        print("\n\t------>El cliente Ha comenzado la conexion<------\n")

        for i in range(len(cache)):
            if message == cache[i][1]:
                existe = 1

        # Hacer el GET
        #no esta en cache
        if existe == 0: 
            socketUrl = s.socket(s.AF_INET, s.SOCK_STREAM)
            socketUrl.connect((message, 80))   
            socketUrl.sendall(b'GET / HTTP/1.1\r\n\r\n')
            
            # recibir respuesta GET
            headReceived = socketUrl.recv(2048)
            header = headReceived.decode("cp437")
            
            # split header para cliente
            header = header.split("<")[0]

            # Guardar en cache
            for i in range(len(cache)):
                if cache[i] == [0,"",""]:
                    cache[i] = [0, message, header]
                    break
                cache[i][0] = cache[i][0] + 1

            # cache esta lleno
            if con > 5:
                cache.remove(max(cache))
                cache.append([0, message, header])
            con = con + 1
                
            
            # cierre de socket usados en TCP
            socketUrl.close()
        
        #esta en cache
        else:
            for i in range(len(cache)):
                if cache[i][1] == message:
                    cache[i][0] = 0
                    header = cache[i][2]

        # respuesta servidor -> cliente
        toSend = str(newServerPort)
        tcpSocketClient.send(toSend.encode())
        print("\n\t------>Envio puerto UDP a cliente<------\n")
        tcpSocketClient.close()
        #------------------------------------------------------> Termino conexion TCP
        
        print("\n")
        for l in cache:
            print((l[0],l[1]))
        print("\n")
        
        #------------------------------------------------------> Inicio conexion UDP
        # Sockets para conexion UDP
        # SOCK_DGRAM -> indica UDP
        udpSocketServ = s.socket(s.AF_INET, s.SOCK_DGRAM)
        udpSocketServ.bind(('', newServerPort))
        print("\n\t------>Inicio conexion UDP con cliente<------\n")
        print('\nServidor UDP escuchando en el puerto:', newServerPort)
        print("\nEsperando respuesta cliente\n")

        message, clientDir = udpSocketServ.recvfrom(2048)
        decoded = message.decode()

        print('Respuesta cliente: ', decoded)
        
        # envio header al cliente
        udpSocketServ.sendto(header.encode(), clientDir)
            
        udpSocketServ.close()
        print("\n\t------>Cierre conexion UDP con cliente<------\n")
        #------------------------------------------------------> End conexion UDP
    else:
        print("\n\t------>El cliente Ha terminado la conexion<------\n")

    with open('cache.txt', 'w') as filehandle:
        json.dump(cache, filehandle)

# cierre conexion TCP
tcpSocketServ.close()

