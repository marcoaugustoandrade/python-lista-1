tamanho = float(input('Informe o tamanho do arquivo (MB): ')) * 8
velocidade = float(input('Informe a velocidade do link de internet (Mbps): '))

print("O tempo de download é de %.2f minutos" % ((tamanho / velocidade) / 60))
