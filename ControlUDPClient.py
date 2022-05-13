from http import server
import socket
import select

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
#FILE_LEN_BYTES = 104857600
FILE_LEN_BYTES = 90000
PACKET_SIZE = 500

def clienteUDPControle(host, port, packetSize, file_len):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data_sent = 0
        server_addrPort = (host, port)
        id_pacote = 0
        s.sendto(bytes(str(id_pacote), 'utf-8')+b"-"*packetSize-1, server_addrPort)

        #Espera primeiro pacote e quando recebe manda o ACK
        while (data_sent < file_len):

            if((file_len-data_sent)+1 < packetSize):
            # pedaço do pacote
                ready = select.select([s], [], [], 2)
                if(ready[0]):
                    #recebeu ACK, manda proximo pacote
                    data = s.recv(packetSize)
                    if data == b"ACK0":
                        s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(file_len-data_sent-1), server_addrPort)
                    else:
                        if id_pacote == 9: id_pacote = 0
                        else: id_pacote += 1
                        s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(file_len-data_sent-1), server_addrPort)
                        data_sent += file_len-data_sent
                else:
                    #nao recebeu ACK, reenvia pacote
                    s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(file_len-data_sent-1), server_addrPort)
            else:
            # pacote inteiro
                ready = select.select([s], [], [], 2)
                if(ready[0]):
                    #recebeu ACK, manda proximo pacote
                    data = s.recv(packetSize)
                    if data == b"ACK0":
                        s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(packetSize-1), server_addrPort)
                    else:
                        if id_pacote == 9: id_pacote = 0
                        else: id_pacote += 1
                        s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(packetSize-1), server_addrPort)
                        data_sent += file_len-data_sent
                else:
                    #nao recebeu ACK, reenvia pacote
                    s.sendto((id_pacote).to_bytes(1, byteorder='big')+b"-"*(packetSize-1), server_addrPort)

    print(f"All {data_sent} bytes of data sent")

if __name__ == "__main__":
    clienteUDPControle(HOST, PORT, PACKET_SIZE, FILE_LEN_BYTES)