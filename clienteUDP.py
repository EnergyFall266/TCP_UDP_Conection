import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FILE_LEN_BYTES = 104857600
# FILE_LEN_BYTES = 90000
PACKET_SIZE = 500

def clienteUDP(host, port, packetSize, file_len = FILE_LEN_BYTES):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((host, port))
        data_sent = 0
        #manda pacote inicial para indicar que o cronometro deve iniciar
        s.send(b"-"*packetSize)

        #envia dadodos enquanto o contador de dados for menor que 100MB
        while(data_sent < file_len):
            if((file_len-data_sent) < packetSize):
                s.send(b"-"*(file_len-data_sent))
                #print(f"Sent {file_len-data_sent}B packet. Total {data_sent}B sent")/
                data_sent += file_len-data_sent
            else:
                s.send(b"-"*packetSize)
                #print(f"Sent {packetSize}B packet. Total {data_sent}B sent")
                data_sent += packetSize
            
    # print(f"All {data_sent} bytes of data sent")

if __name__ == "__main__":
    clienteUDP(HOST, PORT, PACKET_SIZE, FILE_LEN_BYTES)