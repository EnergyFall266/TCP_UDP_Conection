import sys
import serverUDP, serverTCP, ControlUDPServer
import numpy as np
import scipy.stats
import time

#HOST = "127.0.0.1"  # Para executar localmente
HOST = "210.210.210.210" # Para executar em conexão direta a cabo ethernet (IP fixo necessario)
#HOST = "10.81.112.120" # Para execuar na rede interna da unioeste
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def media_intervaloDeConfianca(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m = np.mean(a)
    se = scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h, np.std(a)

def teste_servidor(protocolo, host, port, PacketSize):
    tempo = []
    bytes_recebidos = []
    blocos_recebidos = []
    if protocolo == "TCP":
        for i in range(10):
            print(f'iter: {i}')
            dados = serverTCP.servidorTCP(host, port, PacketSize)
            print(dados)
            tempo.append(dados[0])
            bytes_recebidos.append(dados[1])
            blocos_recebidos.append(dados[2])
            time.sleep(2)
    elif protocolo == "UDP":
        for i in range(10):
            print(f'iter: {i}')
            dados = serverUDP.servidorUDP(host, port, PacketSize)
            tempo.append(dados[0])
            print(dados)
            bytes_recebidos.append(dados[1])
            blocos_recebidos.append(dados[2])
    elif protocolo == "ControleUDP":
        for i in range(10):
            print(f'iter: {i}')
            dados = ControlUDPServer.servidorUDPControle(host, port, PacketSize)
            tempo.append(dados[0])
            bytes_recebidos.append(dados[1])
            blocos_recebidos.append(dados[2])
    else:
        print("Entrada invalida\n")
        print("Entradas aceitas: TCP, UDP, ControleUDP")
        return
        
    tempoStat = media_intervaloDeConfianca(tempo)
    print("Tempo:")
    print(f"Media: {tempoStat[0]} | Intervalo: [{tempoStat[1]}, {tempoStat[2]}] | Desvio Padrão: {tempoStat[3]}")
    byteStat = media_intervaloDeConfianca(bytes_recebidos)
    print("Bytes recebidos:")
    print(f"Media: {byteStat[0]}")
    blocoStat = media_intervaloDeConfianca(blocos_recebidos)
    print("Blocos recebidos:")
    print(f"Media: {blocoStat[0]}")



if __name__ == "__main__":
    teste_servidor(sys.argv[1], HOST, PORT, int(sys.argv[2]))