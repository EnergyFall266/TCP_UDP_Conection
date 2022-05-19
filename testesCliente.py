import sys

# import scipy
import clienteUDP, clienteTCP, ControlUDPClient
import time
import numpy as np
# import scipy.stats

HOST = "210.210.210.210"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# def conta(data, confidence = 0.95):
#     a = 1.0 * np.array(data)
#     n = len(a)
#     m = np.mean(a)
#     se = scipy.stats.sem(a)
#     h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
#     return m, m-h, m+h, np.std(a)

def testes_cliente(protocolo, host, port, packetSize):
    pacotes_enviados = []
    bytes_enviados = []
    if protocolo == "TCP":
        for i in range(10):
            print(f"interação: {i}")
            dado = clienteTCP.clienteTCP(host, port, packetSize)
            pacotes_enviados.append(dado[1])
            bytes_enviados.append(dado[0])
            
            time.sleep(2)
    elif protocolo == "UDP":
        for i in range(10):
            print(f"interação: {i}")
            dado = clienteUDP.clienteUDP(host, port, packetSize)
            pacotes_enviados.append(dado[1])
            bytes_enviados.append(dado[0])
            #time.sleep(2)
    elif protocolo == "ControleUDP":
        for i in range(10):
            print(f"interação: {i}")
            dado = ControlUDPClient.clienteUDPControle(host, port, packetSize) 
            pacotes_enviados.append(dado[1])
            bytes_enviados.append(dado[0])
            # time.sleep(2)
    else:
        print("Entrada invalida\n")
        print("Entradas aceitas: TCP, UDP, ControleUDP")
    # retornoconta_pacotes = conta(pacotes_enviados)
    # print(f"Media {retornoconta_pacotes[0]} | Intervalo {retornoconta_pacotes[1]}{retornoconta_pacotes[2]} | Desvio {retornoconta_pacotes[3]} ")
    # retornoconta_bytes = conta(bytes_enviados)
    # print(f"Media {retornoconta_bytes[0]} | Intervalo {retornoconta_bytes[1]}{retornoconta_bytes[2]} | Desvio {retornoconta_bytes[3]} ")

if __name__ == "__main__":
    testes_cliente(sys.argv[1], HOST, PORT, int(sys.argv[2]))