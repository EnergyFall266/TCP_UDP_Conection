import socket
import time
import select

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
PACKET_SIZE = 512

def servidorUDP(host, port, packetSize):
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        #s.setblocking(0)
        data_received = 0
        blocos_recebidos = 0
        # print(f"Connected by {addr}")

        #espera pelo primeiro pacote para começar a contar
        tempo_inicial = 0
        # print("Waiting for client to connect...")
        while(True):
            ready = select.select([s], [], [], 1)
            if(ready[0]):
                # print("Listeing for first packet")
                data, client = s.recvfrom(packetSize)
                # print("First decoy packet arrived")   
                
                break
        #s.connect(client)
        tempo_inicial = time.time()
        #lê os dados enquento eles sao enviados
        while True:
            #ready = select.select([s], [], [],1)
            #if(ready[0]):
                # print("Received packet")
                data = s.recvfrom(packetSize)[0]
                data_received += len(data)
                blocos_recebidos += 1
                if data == b'encerrou':
                    tempo_final = time.time() - tempo_inicial
                    break
                #print(f"Received {data_received}")
        print(f'All data received. Received {data_received} bytes')
        return tempo_final, data_received, blocos_recebidos

if __name__ == "__main__":
    servidorUDP(HOST, PORT, PACKET_SIZE)