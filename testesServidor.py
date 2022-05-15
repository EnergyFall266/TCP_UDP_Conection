import sys
import serverUDP, serverTCP, ControlUDPServer
import numpy as np
import scipy.stats

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def media_intervaloDeConfianca(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m = np.mean(a)
    se = scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h, np.std(a)

def teste_servidor(protocolo, host, port, PacketSize):
    dados=[]
    if protocolo == "TCP":
        for i in range(10):
            dados.append(serverTCP.servidorTCP(host, port, PacketSize))
        return media_intervaloDeConfianca(dados)
    elif protocolo == "UDP":
        for i in range(10):
            dados.append(serverUDP.servidorUDP(host, port, PacketSize))
        return media_intervaloDeConfianca(dados)
    elif protocolo == "ControleUDP":
        for i in range(10):
            dados.append(ControlUDPServer.servidorUDPControle(host, port, PacketSize))
        return media_intervaloDeConfianca(dados)
    else:
        print("Entrada invalida\n")
        print("Entradas aceitas: TCP, UDP, ControleUDP")



if __name__ == "__main__":
    print(teste_servidor(sys.argv[1], HOST, PORT, int(sys.argv[2])))