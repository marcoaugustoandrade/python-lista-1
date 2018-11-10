# (Python.org.br) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Informe o tamanho do arquivo (MB): ')) * 8
velocidade = float(input('Informe a velocidade do link de internet (Mbps): '))

print("O tempo de download é de %.2f minutos" % ((tamanho / velocidade) / 60))
