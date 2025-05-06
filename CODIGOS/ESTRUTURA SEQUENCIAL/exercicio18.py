'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''


def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    # Convertendo a velocidade da Internet de Mbps para MBps
    velocidade_internet_mbps = velocidade_internet_mbps / 8

    # Calculando o tempo de download em segundos
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps

    # Convertendo o tempo de download de segundos para minutos
    tempo_download_minutos = tempo_download_segundos / 60

    return tempo_download_minutos

def main():
    tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
    velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

    tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

    print("Tempo aproximado de download:", round(tempo_download_minutos, 2), "minutos")

if __name__ == "__main__":
    main()
