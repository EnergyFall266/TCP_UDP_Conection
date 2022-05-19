import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FILE_LEN_BYTES = 104857600
# FILE_LEN_BYTES = 100000
PACKET_SIZE = 500

def clienteUDP(host, port, packetSize, file_len = FILE_LEN_BYTES):
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        #s.connect((host, port))
        #s.bind((host, port+1))
        server_addrPort = (host, port)
        s.connect(server_addrPort)
        data_sent = 0
        blocos_gerados = 0
        #manda pacote inicial para indicar que o cronometro deve iniciar
        #s.send(b"-"*packetSize)
        #s.sendto(b"-"*packetSize, server_addrPort)
        s.sendall(b"-"*packetSize)

        #envia dadodos enquanto o contador de dados for menor que 100MB
        while(data_sent < file_len):
            if((file_len-data_sent) < packetSize):
                #s.send(b"-"*(file_len-data_sent))
                s.sendto(b"-"*(file_len-data_sent), server_addrPort)
                #s.sendall(b"-"*(file_len-data_sent))
                # print(f"Sent {file_len-data_sent}B packet. Total {data_sent}B sent")
                data_sent += file_len-data_sent
            else:
                #s.send(b"-"*packetSize)
                s.sendto(b"-"*packetSize, server_addrPort)
                #s.sendall(b"-"*packetSize)
                # print(f"Sent {packetSize}B packet. Total {data_sent}B sent")
                data_sent += packetSize
            blocos_gerados += 1
        s.sendto(b"encerrou", server_addrPort)
    print(f"All {data_sent} bytes of data sent. Blocos gerados: {blocos_gerados}")
    # print(f"All {data_sent} bytes of data sent")
    return data_sent, blocos_gerados

if __name__ == "__main__":
    clienteUDP(HOST, PORT, PACKET_SIZE, FILE_LEN_BYTES)