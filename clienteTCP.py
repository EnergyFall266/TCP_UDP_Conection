import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FILE_LEN_BYTES = 104857600
# FILE_LEN_BYTES = 1000
PACKET_SIZE = 500

def clienteTCP(host, port, packetSize, file_len):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data_sent = 0

        #envia dadodos enquanto o contador de dados for menor que 100MB
        while(data_sent < file_len):
            if((file_len-data_sent) < packetSize):
                s.send(b"-"*(file_len-data_sent))    
            else:
                s.send(b"-"*packetSize)
            data_sent += packetSize
    print("All data sent")

if __name__ == "__main__":
    clienteTCP(HOST, PORT, PACKET_SIZE, FILE_LEN_BYTES)