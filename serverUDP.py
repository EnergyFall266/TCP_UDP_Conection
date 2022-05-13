import socket
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
PACKET_SIZE = 500

def servidorTCP(host, port, packetSize):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        # s.listen()
        # conn, addr = s.accept()
        data_received = 0
        # print(f"Connected by {addr}")

        #espera pelo primeiro pacote para começar a contar
        tempo_inicial = 0

        while True:
            data = s.recv(packetSize)
            if data:
                print(data)
                tempo_inicial = time.time()
                break

        #lê os dados enquento eles sao enviados
        while True:
            data = s.recv(packetSize)
            data_received += len(data)
            #print(data_received)
            print(data)
            if not data:
                tempo_final = time.time() - tempo_inicial
                break
            #print(f'Server sent: {conn.send(data)} bytes')
        print(f'All data received.\nReceived {data_received} bytes in {tempo_final} seconds')
        return tempo_final

if __name__ == "__main__":
    servidorTCP(HOST, PORT, PACKET_SIZE)