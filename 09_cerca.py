# (BACKES, 2012) Faça um programa para ler as dimensões de um terreno (comprimento (C) e largura (L)), bem como o preço do metro de tela (P). Imprima o custo para cercar este mesmo terreno com tela.

comprimento = float(input('Informe o comprimento do terreno (mts): '))
largura = float(input('Informe a largura do terreno (mts): '))
preco = float(input('Informe o preço do metro de tela: R$ '))

print("O custo para cercar o terreno é de R$ %.2f" % ((comprimento +largura) * preco))
