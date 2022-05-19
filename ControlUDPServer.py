import socket
import time
import select

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
PACKET_SIZE = 512

def servidorUDPControle(host, port, packetSize):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        s.setblocking(0)
        data_received = 0
        blocos_recebidos = 0
        #espera pelo primeiro pacote para começar a contar
        tempo_inicial = 0
        id_pacote = 0
        # print("Waiting for client to connect...")
        
        while(True):
            ready = select.select([s], [], [], 2)
            if(ready[0]):
                # print("Listeing for first packet")
                data = s.recvfrom(packetSize) #USAR RCVFROM pra conseguir o ip do cliente e mandar ack
                # print("First decoy packet arrived")
                clientAddrPort = data[1]
                tempo_inicial = time.time()
                s.sendto(b"ACK1",clientAddrPort)
                break
        #lê os dados enquento eles sao enviados
        while True:
            ready = select.select([s], [], [], 2)
            if(ready[0]):
                # print("Received packet")
                data = s.recv(packetSize)
                
                if data == b"encerrou":
                    break
                data_received += len(data)
                # DEVOLVE UM ACK com sendto
                s.sendto(b"ACK1", clientAddrPort)
                blocos_recebidos += 1
                #print(f"Received {data_received}")
            else:
                # DEVOLVE UM NACK com sendto
                s.sendto(b"ACK0", clientAddrPort)
                print("ACK0\n")

        tempo_final = time.time() - tempo_inicial
        # print(f'All data received. Received {data_received} bytes')
        
        return tempo_final, data_received, blocos_recebidos

if __name__ == "__main__":
    print(servidorUDPControle(HOST, PORT, PACKET_SIZE))