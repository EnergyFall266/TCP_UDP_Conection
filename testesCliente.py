import sys
import clienteUDP, clienteTCP, ControlUDPClient
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def testes_cliente(protocolo, host, port, packetSize):
    if protocolo == "TCP":
        for i in range(10):
            clienteTCP.clienteTCP(host, port, packetSize)
            time.sleep(2)
    elif protocolo == "UDP":
        for i in range(10):
            clienteUDP.clienteUDP(host, port, packetSize)
            time.sleep(2)
    elif protocolo == "ControleUDP":
        for i in range(10):
            ControlUDPClient.clienteUDPControle(host, port, packetSize) 
            time.sleep(2)
    else:
        print("Entrada invalida\n")
        print("Entradas aceitas: TCP, UDP, ControleUDP")

if __name__ == "__main__":
    testes_cliente(sys.argv[1], HOST, PORT, int(sys.argv[2]))