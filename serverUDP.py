import socket
import time
import select

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
PACKET_SIZE = 512

def servidorTCP(host, port, packetSize):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        s.setblocking(0)
        # s.listen()
        # conn, addr = s.accept()
        data_received = 0
        # print(f"Connected by {addr}")
        #s.setblocking(0)

        #espera pelo primeiro pacote para começar a contar
        tempo_inicial = 0
        while(True):
            print("entrei\n")
            ready = select.select([s], [], [], 2)
            if(ready[0]):
                print("Listeing for first packet")
                data = s.recv(packetSize)
                print("First decoy packet arrived")
                tempo_inicial = time.time()
                break

        #lê os dados enquento eles sao enviados
        while True:
            ready = select.select([s], [], [], 2)
            if(ready[0]):
                print("Received packet")
                data = s.recv(packetSize)
                data_received += len(data)
                print(data_received)

            else:
                tempo_final = time.time() - tempo_inicial
                print(f"Total: {data_received}")
                break
        print(f'All data received.\nReceived {data_received} bytes in {tempo_final} seconds')
        return tempo_final

if __name__ == "__main__":
    servidorTCP(HOST, PORT, PACKET_SIZE)